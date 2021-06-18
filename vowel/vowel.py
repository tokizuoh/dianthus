import sys

def extract(roman: str) -> str:
    vowel = 'aiueo'

    result = ''
    should_skip = False
    for i in range(len(roman)):
        if should_skip:
            should_skip = False
            continue
        
        r = roman[i]

        if r in vowel:
            result += r
            continue

        if r == 'n':
            if i + 1 < len(roman):
                nr = roman[i + 1]
                if nr in vowel:
                    should_skip = True
                    result += nr
                else:
                    result += r
            else:
                result += r
            continue
        
        if i + 1 < len(roman):
            nr = roman[i + 1]
            if r == nr:
                result += 'x'
        else:
            result += r

    return result    