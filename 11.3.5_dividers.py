n = int(input())
dividers = []

for i in range(1, n+1):
    if n % i == 0:
        dividers.append(i)
    else:
        continue
print(dividers)