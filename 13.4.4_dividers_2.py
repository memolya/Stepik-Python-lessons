# объявление функции
def get_factors(num):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += 1
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))