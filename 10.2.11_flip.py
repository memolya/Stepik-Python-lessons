n = input()

for i in range(len(n)):
    first_h = n.find('h')
    before_first_h = n[:n.find('h')]

    second_h = n.rfind('h')
    after_second_h = n[second_h+1:]

    between = n[first_h+1:second_h]
    between = between[::-1]

#print('before_first_h =', before_first_h) -debug
#print('after_second_h =', after_second_h ) -debug
#print('between =', between) -debug

print(before_first_h, 'h', between, 'h', after_second_h, sep ='')