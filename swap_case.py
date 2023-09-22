# Problem : https://www.hackerrank.com/challenges/swap-case

def swap_case(s):
    transform_phrase = []

    for letter in s:
        if letter.isupper():
            letter_trans = letter.lower()
            transform_phrase.append(letter_trans)
        elif letter.islower():
            letter_trans = letter.upper()
            transform_phrase.append(letter_trans)
        else:
            transform_phrase.append(letter)

    string_final = ''.join(transform_phrase)

    return string_final
