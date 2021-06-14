import sys
import pykakasi


class Word:
    def __init__(self, original: str, roman_letters: str):
        self.original = original
        self.roman_letters = roman_letters


class InvalidArgsError(Exception):
    pass


def convertRomanLetters(sentence: str) -> [Word]:
    kks = pykakasi.kakasi()
    res = kks.convert(sentence)
    words = []
    for item in res:
        words.append(Word(original=item['orig'], roman_letters=item['hepburn']))
    return words


def main():
    args = sys.argv
    if len(args) == 1:
        raise InvalidArgsError
    
    target = args[1]
    words = convertRomanLetters(sentence=target)
    
    for w in words:
        print(w.original, w.roman_letters)


if __name__ == "__main__":
    main()