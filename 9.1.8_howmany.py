s = input()
count_star, count_plus = 0, 0
for i in range(0, len(s)):
    if s[i] in ('*'):
        count_star += 1
    if s[i] in ('+'):
        count_plus += 1
print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_star, 'раз')