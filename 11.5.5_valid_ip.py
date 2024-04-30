ip = input()
result = ip.split('.')
result = list(map(int, result))
Flag = True
print(result)

for i in range(len(result)):
    if result[i] > 255:
        Flag = False
        break
    else:
        continue

if Flag == False:
    print('НЕТ')
else:
    print('ДА')