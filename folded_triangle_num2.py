n = int(input())
temp = 0
counter = 1
for column in range(1, n+1+(n-1)):
    if column > n and column > 0:
        temp = n-counter
        print(temp, end='')
        counter += 1
    else:
        print(column, end='')
