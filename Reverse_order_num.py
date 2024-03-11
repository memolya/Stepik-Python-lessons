num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit) #Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.