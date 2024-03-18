amount = int(input())
cubes = 0
all_cubes_output = []

for i in range(amount):
    to_cubes = int(input())
    #print('Enter number', [i])
    cubes = to_cubes ** 3
    #print('Cube  of', to_cubes, 'equals to', cubes)
    all_cubes_output.append(cubes)
print(all_cubes_output)

