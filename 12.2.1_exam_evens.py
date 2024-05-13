n = int(input())
numbers = list(range(1, n+1))
result = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(numbers[i])

print(result)
