# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep = '')

# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию

print_fio(name, surname, patronymic)

# print(surname.upper()[0] + name.upper()[0] + patronymic.upper()[0])
