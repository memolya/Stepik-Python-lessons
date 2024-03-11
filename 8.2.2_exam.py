n = 8 #не 7, а 8, столько раз подаем инпут в x
count = 0
maximum = -10**12 #не 1000, а абсолютная величина не превышает 10**12
for i in range(n): #не  range(1, n + 1), а range(n)
    x = int(input())
    if x % 4 == 0: #не //, a %
        count += 1
        if x > maximum: #не <, а > #ПОСЛЕДОВАТЕЛЬНОСТЬ целых чисел, поэтому в maximum всегда запишется максимальное (последнее) введенное число %4 ==0
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')