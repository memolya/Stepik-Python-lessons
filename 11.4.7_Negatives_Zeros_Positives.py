negatives = []
zeros = []
positives = []
result = []

#amount of numbers for input
n = int(input())

#numbers input
for i in range(n):
    number = int(input())

    if number < 0:
        negatives.append(number)

    elif number == 0:
         zeros.append(number)

    elif number > 0:
        positives.append(number)

result = negatives + zeros + positives
print(*result, sep = '\n')




