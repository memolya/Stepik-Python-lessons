# объявление функции
def find_all(target, symbol):
    result = []
    for i in range(len(s)):
        if char in s[i]:
            result.append(i)
    return result

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))