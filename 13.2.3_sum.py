# объявление функции
def print_digit_sum(num):
    res = [int(x) for x in str(n)]
    print(sum(res))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)