n = int(input())
consequent_flag = False
while n // 10 != 0:
    last_num = n % 10
    n = n // 10
    before_last_num = n % 10
    if last_num > before_last_num: #чтобы сразу остановить цикл, если числа идут не по возрастанию справа налево
        consequent_flag = False
        break
    else:
        consequent_flag = True
if consequent_flag == True:
    print('YES')
else:
    print('NO')