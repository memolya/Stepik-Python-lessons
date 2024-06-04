# объявление функции
from math import factorial

def compute_binom(n, k):
    result = factorial(n) / (factorial(k) * factorial(n-k))
    return int(result)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))