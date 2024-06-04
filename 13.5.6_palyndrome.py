# объявление функции
def is_palindrome(text):
    text = []

    for i in range(len(txt)):
        if txt[i].isalpha() == True:
            text.append(txt[i])

    text = ''.join(text).lower()

    if text[:] == text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))