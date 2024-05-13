numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

result = sum(numbers)
print(*numbers, sep = '+', end = '')
print('=', result, sep = '')