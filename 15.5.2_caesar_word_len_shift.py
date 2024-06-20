from math import *
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []
import re
def convert():
    for word in by_word:
        for i in range(len(word)):
            shift = len(word)

            if not word[i].isalpha():
                result.append(word[i])

            else:
                base_element_index = english_alphabet.find(word[i].casefold())
                new = base_element_index + shift

                if new <= 25:
                    result.append(english_alphabet[new])

                    # if text[i] > 25 - we take away 26 from index (so we can get the remaining index and assign it - it will be the index from the start)
                else:
                    new -= 26
                    result.append(english_alphabet[new])
    # print('Result:')
    register()

def register():
    res = []
    for i in range(len(result)):
        if text[i].isalpha():
            if text[i].islower():
                res.append(result[i].lower())
            else:
                res.append(result[i].upper())
        else:
            res.append(result[i])

    print(*res, sep = '')

# print('Введите текст: ')
text = input()
by_word = re.findall(r"[\w']+|[.,!?;\"\s=)(\/+*-]", text)
convert()