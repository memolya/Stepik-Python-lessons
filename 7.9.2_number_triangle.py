n = int(input())
for i in range(1, n + 1):  # строки
    for j in range(1, i + 1): # столбцы на возрастание
        print(j, end='')
    for j in range(i - 1, 0, -1): #столбцы на убывание
        print(j, end='')
    print()