# объявление функции
singles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
singles_count = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}
twofolds_count = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
                  16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
                  20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
def number_to_words(num):
    if n in singles:
        return singles_count.get(n)

    elif n in twofolds_count:
        return twofolds_count.get(n)

    elif 21 <= n <= 39:
        tens = n // 10
        units = n % 10
        result = singles_count.get(tens) + 'дцать' + ' ' + singles_count.get(units)
        return result

    elif 41 <= n <= 49:
        units = n % 10
        return twofolds_count.get(40) + ' ' + singles_count.get(units)

    elif 51 <= n <= 89:
        tens = n // 10
        units = n % 10
        result = singles_count.get(tens) + 'десят' + ' ' + singles_count.get(units)
        return result

    elif 91 <= n <= 99:
        units = n % 10
        result = 'девяносто' + ' ' + singles_count.get(units)
        return result



# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
