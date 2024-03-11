#s = 'Python rocks!'
#print(len(s))

#s = 'Python rocks!'
#print(s[3])

#s = 'Python rocks!'
#print(s[1:5])

#s = '    Python rocks!     '
#print(s.strip())

#s = 'Python rocks!'
#print(s.upper())

#s = 'Python rocks!'
#print(s.replace('o', '@'))

#n = input()
#for i in range (len(n)):
    #if i == 0 or i % 3 == 0:
        #continue
    #else:
        #print(n[i], end ='')

#n = input()
#n = n.replace('1', 'one')
#print(n)

#n = input()
#n = n.replace('@', '')
#print(n)

n = input()
if n.count('f') < 1: #if no 'f's in word - we print -2
    print('-2')
elif n.count('f') == 1: #if 1 'f' in word - we print -1
    print('-1')
else:
    n = n.replace('f', 'x', 1)
    print(n.find('f')) #if >1 'f's in word - we replace the first 'f' and look for the first 'f' that remains






