n = int(input())
numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

del numbers[1::2]

print(numbers)