import sys
import pykakasi
import sqlite3


class Word:
    def __init__(self, word_id: int, lemma: str, roman: str):
        self.word_id = word_id
        self.lemma = lemma
        self.roman = roman


class InvalidArgsError(Exception):
    pass


# def convertRomanLetters(sentence: str) -> [Word]:
#     kks = pykakasi.kakasi()
#     res = kks.convert(sentence)
#     words = []
#     for item in res:
#         words.append(Word(original=item['orig'], roman_letters=item['hepburn']))
#     return words



def main():
    con = sqlite3.connect('wnjpn.db')
    cur = con.cursor()
    cur.execute("select * from word where lang='jpn'")
    for r in cur:
        print(r)

    # args = sys.argv
    # if len(args) == 1:
    #     raise InvalidArgsError
    
    # target = args[1]
    # words = convertRomanLetters(sentence=target)
    
    # for w in words:
    #     print(w.original, w.roman_letters)


if __name__ == "__main__":
    main()