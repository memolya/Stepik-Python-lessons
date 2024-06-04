# put your python code here
import math as m

# объявление функции
def solve(a, b, c):
    result = []

    d = pow(b, 2) - 4 * a * c
    if d == 0:
        x_1 = -b / (2 * a)
        x_2 = x_1
        result.append(x_1)
        result.append(x_2)

    elif d > 0:
        x_1 = (-b + m.sqrt(d)) / (2 * a)
        x_2 = (-b - m.sqrt(d)) / (2 * a)
        result.append(x_1)
        result.append(x_2)
        result.sort()

    return result

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)