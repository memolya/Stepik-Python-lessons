n = input()
if n.count('f') < 1: #if no 'f's in word - we print -2
    print('-2')
elif n.count('f') == 1: #if 1 'f' in word - we print -1
    print('-1')
else:
    n = n.replace('f', 'x', 1)
    print(n.find('f')) #if >1 'f's in word - we replace the first 'f' and look for the first 'f' that remains