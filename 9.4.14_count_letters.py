n = input()
if 'f' in n and n.count('f') == 1:
    print(n.find('f'))
elif n.count('f') > 1:
    print((n.find('f')), (n.rfind('f')), sep=' ')
if 'f' not in n:
    print('NO')