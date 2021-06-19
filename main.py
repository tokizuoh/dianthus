import os
import csv
import argparse
import datetime
import sqlite3

import pykakasi
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from dotenv import load_dotenv

from vowel import vowel


class Word:
    def __init__(self, word_id: int, lemma: str, roman: str, vowels: str):
        self.word_id = word_id
        self.lemma = lemma
        self.roman = roman
        self.vowels = vowels


class InvalidArgsError(Exception):
    pass


def convert_roman(lemma: str) -> str:
    kks = pykakasi.kakasi()
    res = kks.convert(lemma)
    roman = ""

    is_sentence = False
    for item in res:
        if len(roman) > 0:
            is_sentence = True
            break
        roman =item['hepburn']
    
    if is_sentence:
        return ""
    else:
        return roman


def get_now_time() -> str:
    dt_now = datetime.datetime.now()
    now_str = dt_now.strftime('%Y%m%d_%H%M%S')
    return now_str


def generate_roman_csv():
    con = sqlite3.connect('wnjpn.db')
    cur = con.cursor()
    cur.execute("select * from word where lang='jpn'")
    words = []
    for r in cur:
        word_id = r[0]
        lemma = r[2]
        roman = convert_roman(lemma=lemma)
        vowels = vowel.extract(roman)
        if len(roman) == 0:
            continue
        word = Word(word_id=word_id, lemma=lemma, roman=roman, vowels=vowels)
        words.append(word)

    now_time = get_now_time()
    output_csv_file_path = './csv/{}.csv'.format(now_time)
    with open(output_csv_file_path, 'w') as f:
        writer = csv.writer(f)
        for word in words:
            row = [word.word_id, word.lemma, word.roman, word.vowels]
            writer.writerow(row)


def get_recent_update_csv_file_path() -> str:
    directory_path = './csv'
    files = os.listdir(directory_path)
    file_name = sorted(list(filter(lambda x: not x.startswith('original'), files)))[-1]
    file_path = '{}/{}'.format(directory_path, file_name)
    return file_path


def get_same_vowel_words(vowels: str) -> [Word]:
    file_path = get_recent_update_csv_file_path()

    result = []

    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] == vowels:
                word = Word(word_id=row[0], lemma=row[1], roman=row[2], vowels=row[3])
                result.append(word)

    return result


def upload_blob():
    load_dotenv('.env')
    firebase_credential_file_path = os.environ.get('FIREBASE_CREDENTIAL_FILE_PATH')
    firebase_storage_bucket = os.environ.get('FIREBASE_STORAGE_BUCKET')

    cred = credentials.Certificate(firebase_credential_file_path)
    firebase_admin.initialize_app(cred, {'storageBucket': firebase_storage_bucket})
    
    bucket = storage.bucket()

    destination_blob_name = 'demo.csv'
    source_file_name = get_recent_update_csv_file_path()

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('success')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen', action='store_true', help='generate csv on ./csv/')
    parser.add_argument('--vow', action='store_true', help='add column vowel to ./csv/original.csv (create new .csv)')
    parser.add_argument('--demo', action='store_true', help='return words with the same vowel')
    parser.add_argument('--upload', action='store_true', help='upload csv to aws-s3')
    args = parser.parse_args()
    
    args_dict = vars(args)
    if args_dict['gen']:
        generate_roman_csv()
    elif args_dict['vow']:
        # [TODO]: Write vowel extraction logic.
        # [TODO]: Allow sorting by vowel.
        a = vowel.extract('amana')
    elif args_dict['demo']:
        target = vowel.extract(input("INPUT: "))
        print()
        words = get_same_vowel_words(target)
        
        for word in words:
            print(word.lemma, word.roman, word.vowels)
    elif args_dict['upload']:
        upload_blob()


if __name__ == "__main__":
    main()