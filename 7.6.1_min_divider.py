# put your python code here
n = int(input())
for i in range(2, n+1):
    if n % i == 0:
        break
print(i)