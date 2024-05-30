n = int(input())
max_n = 0 #не было этой переменной
while n > 0:
    max_n = n % 10
    n //= 10 # было %
print(max_n) #тут был n