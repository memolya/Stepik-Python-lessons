# объявление функции
def get_days(month):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    if num == 2:
        result = 28
    elif num in days_31:
        result = 31
    else:
        result = 30
    return result

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))