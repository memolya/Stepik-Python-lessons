from math import *
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

def caesar_cypher_ru(text, shift):

    for i in range(len(text)):

        if not text[i].isalpha():
            result.append(text[i])

        else:
            base_element_index = russian_alphabet.find(text[i].casefold()) #casefold in brackets - it doesn't inherit casefold from prev string

            if direction == 'ш' or direction == 'c':
                new = base_element_index + shift
            else:
                new = base_element_index - shift


            if new <= 31:
                result.append(russian_alphabet[new])

            #if text[i] > 31 - we take away 32 from index (so we can get the remaining index and assign it - it will be the index from the start)
            else:
                new -= 32
                result.append(russian_alphabet[new])

    print('Результат:')
    register()

def caesar_cypher_en(text, shift):

    for i in range(len(text)):

        if not text[i].isalpha():
            result.append(text[i])

        else:
            base_element_index = english_alphabet.find(text[i].casefold())

            if direction == 'ш' or direction == 'c':
                new = base_element_index + shift
            else:
                new = base_element_index - shift

            if new <= 25:
                result.append(english_alphabet[new])

                #if text[i] > 25 - we take away 26 from index (so we can get the remaining index and assign it - it will be the index from the start)
            else:
                new -= 26
                result.append(english_alphabet[new])

    print('Result:')
    register()

def register():
    res = []
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                res.append(result[i].lower())
            else:
                res.append(result[i].upper())
        else:
            res.append(text[i])

    print(*res, sep = '')

print('Введите направление шифрования: шифрование (ш/c) /дешифрование (д/d)')
direction = input()
print('Введите язык шифрования: ру/en ')
language = input()
print('Введите шаг сдвига (сдвиг осуществляется вправо): ')
shift = int(input())
print('Введите текст: ')
text = input()

if (language == 'ру' and
        shift != 0):
    caesar_cypher_ru(text, shift)
elif (language == 'en' and
        shift != 0):
    caesar_cypher_en(text, shift)
#when the shift is unknown and we need all variants
else:
        if language == 'ру':
            for z in range(1, 33):
                shift = z
                print(shift)
                caesar_cypher_ru(text, shift)
                result = []

        else:
            for z in range(1, 26):
                shift = z
                print(shift)
                caesar_cypher_en(text, shift)
                result = []

