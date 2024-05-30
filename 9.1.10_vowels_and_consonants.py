alphabet = input()
counter_vowels = 0
counter_consonants = 0
for i in range(len(alphabet)):
    if alphabet[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        counter_vowels += 1
    if alphabet[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        counter_consonants += 1
print('Количество гласных букв равно', counter_vowels)
print('Количество согласных букв равно', counter_consonants)
