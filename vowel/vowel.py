def extract(roman: str) -> str:
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