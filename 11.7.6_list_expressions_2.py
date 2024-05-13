numbers = [int(x) for x in input().split()]
cubes = [numbers[i]**3 for i in range(len(numbers))]
print(*cubes, sep = ' ')