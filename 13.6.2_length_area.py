import math

# объявление функции
def get_circle(radius):
    c = 2 * math.pi * r
    s = math.pi * r**2
    return c, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)