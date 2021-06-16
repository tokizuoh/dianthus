import sys
import sqlite3
import datetime

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

def main():
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

    output_csv_file_path = './csv/'.format
    # with open('./csv/debug_{}.csv', )
    print(get_now_time())
    # args = sys.argv
    # if len(args) == 1:
    #     raise InvalidArgsError
    
    # target = args[1]
    # words = convertRomanLetters(sentence=target)
    
    # for w in words:
    #     print(w.original, w.roman_letters)


if __name__ == "__main__":
    main()