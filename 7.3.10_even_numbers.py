# put your python code here
counter = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        flag = True
        if flag == True:
            counter += 1
if counter == 10:
    print('YES')
else:
    print('NO')
