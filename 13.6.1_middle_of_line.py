# объявление функции
def get_middle_point(x1, y1, x2, y2):
    a = (x_1 + x_2) / 2
    b = (y_1 + y_2) / 2
    return a, b

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)