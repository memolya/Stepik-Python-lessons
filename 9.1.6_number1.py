s = input()
sum = 0
for i in range(0, len(s)):
    num = int(s[i]) #на каждой итерации цикла преобразуем строковое число в int число, чтобы складывать
    sum += num
print(sum)