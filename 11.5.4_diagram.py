numbers = input()
result = numbers.split()
result = list(map(int, result))

for i in range(len(result)):
    print('+'* result[i], end = '\n')