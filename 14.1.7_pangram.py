# объявление функции

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_pangram(text):
    text = text.lower()
    has_all = all([char in text for char in alphabet])
    return has_all

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))