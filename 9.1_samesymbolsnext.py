s = input()
counter = 0
holder_1, holder_2 = 0, 0
for i in range (0, len(s)-1): #for i in range(len(text)) - цикл отработает "количество символов в строке" раз. А т.к ,по логике этой задачи, последний символ сравнивать не с чем - мы записываем   for i in range(len(text) - 1)
    holder_1 = s[i]
    holder_2 = s[i+1]
    if holder_1 == holder_2:
        counter += 1
print(counter)
