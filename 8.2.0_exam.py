n = int(input()) #добавила int
s = 0
while n > 0: #не 10, а 0
    if n % 2 == 0: #не 1, а 0
        s += n % 10 #не =, а +=
    n //= 10
print(s)