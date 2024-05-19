# объявление функции
def draw_triangle(fill, base):
    for j in range(1, base+1):
        if (base + 1) // j >= 2:
            print(fill * j, sep = '', end = '\n')
        else:
            print(fill * ((base + 1) - j), sep='', end='\n')

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)