# объявление функции
def draw_triangle(base, height):

    for z in range(1, 9):
        print(' ' * (8 - z), sep = '', end = '')
        print('*' * ((z-1) + z), sep = '', end = '\n')

# основная программа
draw_triangle(15, 8)  # вызов функции