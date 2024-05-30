# put your python code here
counter1 = 0
counter2 = 0
n = int(input())
for i in range(1, n+1):
    if i % 2 != 0:
        counter1 += i
    else:
        counter2 -= i
print(counter1 + counter2)
