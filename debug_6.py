n = int(input()) #не было int
product = 1 #было n % 10
while n != 0: #было >=10
    digit = n % 10
    product *= digit #укоротила
    n //= 10
print(product)