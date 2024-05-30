n = int(input())
holder_1 = 0 #сюда кладем цифру 1 для сравнения
max_holder = 0
min_holder = 9
while n != 0: #цикл продолжается, пока всё число не расщепим до первого разряда
    holder_1 = n % 10 #отделяем последнюю цифру
    n = n // 10  # отделяем последнюю цифру от ввода, чтобы не мешала
    if holder_1 > max_holder:
        max_holder = holder_1
    if holder_1 < min_holder:
        min_holder = holder_1
print('Максимальная цифра равна', max_holder)
print('Минимальная цифра равна', min_holder)

