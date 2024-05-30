n = input()
for i in range (len(n)):
    if i == 0 or i % 3 == 0:
        continue
    else:
        print(n[i], end ='')