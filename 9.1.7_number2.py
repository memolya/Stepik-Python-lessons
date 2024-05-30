s = input()
for i in range(0, len(s)):
    if s[i] in ('0123456789'):
        print('Цифра')
        break
else:
    print('Цифр нет')