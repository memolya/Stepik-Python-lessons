import math
n = int(input())
fact_sum = 0
for i in range(1, n+1):
    x = math.factorial(i)
    fact_sum += x
print(fact_sum)

