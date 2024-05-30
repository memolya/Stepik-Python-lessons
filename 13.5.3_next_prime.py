# объявление функции
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель
    return True


def get_next_prime(num):
    num += 1
    while is_prime(num) != True:
        num += 1
        if is_prime(num) == True:
            break
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
