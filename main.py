import csv
import sys
import sqlite3
import datetime
import argparse

import pykakasi


class Word:
    def __init__(self, word_id: int, lemma: str, roman: str):
        self.word_id = word_id
        self.lemma = lemma
        self.roman = roman


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
        if len(roman) == 0:
            continue
        word = Word(word_id=word_id, lemma=lemma, roman=roman)
        words.append(word)

    now_time = get_now_time()
    output_csv_file_path = './csv/{}.csv'.format(now_time)
    with open(output_csv_file_path, 'w') as f:
        writer = csv.writer(f)
        for word in words:
            row = [word.word_id, word.lemma, word.roman]
            writer.writerow(row)


def extract_vowel(roman: str) -> str:
    vowel = 'aiueo'

    result = ''
    should_skip = False
    for i in range(len(roman)):
        if should_skip:
            should_skip = False
            continue
        
        if roman[i] in vowel:
            result += roman[i]
        elif roman[i] == 'n':
            if i + 1 < len(roman):
                r_next = roman[i + 1]
                if r_next in vowel:
                    should_skip = True
                    result += r_next
                else:
                    result += roman[i]
            else:
                result += roman[i]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen', action='store_true', help='generate csv on ./csv/')
    parser.add_argument('--vow', action='store_true', help='add column vowel to ./csv/original.csv (create new .csv)')
    args = parser.parse_args()
    
    args_dict = vars(args)
    if args_dict['gen']:
        generate_roman_csv()
    elif args_dict['vow']:
        # [TODO]: Write vowel extraction logic.
        # [TODO]: Allow sorting by vowel.
        a = extract_vowel("amana")
        print(a)

if __name__ == "__main__":
    main()