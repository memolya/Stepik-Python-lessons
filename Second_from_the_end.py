#отрезать с конца по 1 цифре, пока остаток от деления на 10 не будет < 1. Тогда напечатать вторую цифру (она будет последним остатком от деления на 10)
num = int(input())
while num // 10 > 1: #тоже можно, но не работает на числа, начинающиеся со 100 - сразу печатает last_digit, тк под это условие надо >= 1.
    last_digit = num % 10
    num = num // 10
print(last_digit)

num = int(input())
while num // 10 >= 1: #пофиксила ошибку с проверкой числа 123 способа выше
    #если >= 11 - будет 3 цифра, если >=111 - 4, и тд
    last_digit = num % 10
    num = num // 10
print(last_digit)

num = int(input())
while num > 100: #способ из комментов, когда мы проверяем число на двузначность
    last_digit = num % 10
    num = num // 10
print(num % 10)
