# объявление функции
def convert_to_miles(km):
    miles = num * 0.6214
    result = round(miles, 4) #4 digits after the comma
    return result

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))