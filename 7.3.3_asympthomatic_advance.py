# put your python code here
import math as m
counter = 0
n = int(input())
for i in range(n):
    counter += 1 / (i+1)
print(counter - m.log(n))
