numbers_list = input().split()
counter = 0

for j in range(len(numbers_list)):
    for i in range(j+1, (len(numbers_list))):
        if numbers_list[j] == numbers_list[i]:
            counter += 1

print(counter)