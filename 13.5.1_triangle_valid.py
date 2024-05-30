def is_valid_triangle(side1, side2, side3):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

# def is_valid_triangle(side1, side2, side3):
#     sides = sorted([side1, side2, side3])  # создаём отсортированный список из сторон
#
#     return sides[0] + sides[1] > sides[2]  # проверяем, минимальная и средняя стороны больше максимальной
#
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))