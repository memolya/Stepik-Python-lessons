# print(*[i**2 for i in map(int, input().split()) if i % 2 == 0 and i**2 % 10 != 4], sep = ' ')
print(*[int(i)**2 for i in input().split if int(i) % 2 == 0 and int(i)**2 % 10 != 4])