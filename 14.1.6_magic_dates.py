# объявление функции
def is_magic(date):

    date_list = date.split('.')
    multiply = int(date_list[0])*int(date_list[1])
    last_num = int(date_list[2]) % 100

    if multiply == last_num:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))