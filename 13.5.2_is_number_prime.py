# объявление функции
def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))


# # объявление функции
# def is_prime(num):
#     if num == 1:
#         return False  # число 1 не является простым
#
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False  # сразу возвращает False, когда находим делитель
#
#     return True
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))