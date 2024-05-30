n = int(input())
max_digit = -1 #было n % 10, 0 тоже не подошел, тк 0 % 3 == 0
digit = 0 #не было строки #можно было не вводить, ввести прямо в теле цикла
while n != 0: #было >, можно было оставить
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: #было <
            max_digit = digit #было наоборот
    n = n // 10 #было %
if max_digit % 3 != 0: #было if max_digit % 3 == 0
    print('NO')
else:
    print(max_digit)