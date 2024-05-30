a, b = int(input()), int(input())
for x in range(a, b+1):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    if count == 2:
        print(x)

