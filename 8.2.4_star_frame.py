n = int(input())
star = str("*")
for i in range(n): # по вертикали
    if i == 0 or i == n-1:
        print(star * 19)
    else:
        print(star, star, sep='                 ')
print()
