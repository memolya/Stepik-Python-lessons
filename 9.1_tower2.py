s = input()
for i in range(len(s)-1, -1, -1): #если длина строки s равна len(s), то при положительной нумерации слева направо, последний элемент имеет индекс равный len(s) - 1
    #len(s)-1 - последний символ при положительной нумерации (abc - c[3-1=2]). -1 граница - последний символ при обратной нумерации (c[0]). Граница -1 не включается. -1 шаг - в обратную сторону шагаем
    print(s[i], sep = '/n' )