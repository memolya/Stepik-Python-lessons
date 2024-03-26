numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
square_all = []
#need to print a sum of squares of the list elements
for num in numbers:
    square = num**2
    square_all.append(square)
print(sum(square_all))

#2nd option

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
square_all = []

#need to print a sum of squares of the list elements
for num in numbers:
    square_all.append(num**2)

print(sum(square_all))
