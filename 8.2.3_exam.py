n = 4
count = 0
maximum = -10**8 #не 999, а "вводимые числа по абсолютной величине не превышают 10**8"
for i in range(n): #не (1, n + 1), а (n)
    x = int(input())
    if x % 2 != 0: 
        count += 1
        if x > maximum:
            maximum = x #x, а не i
            #break не нужен
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')