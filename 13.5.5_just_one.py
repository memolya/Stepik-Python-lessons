# объявление функции
def is_one_away(word1, word2):
    counter = 0

    if len(txt1) != len(txt2):
        return False

    for i in range(len(txt1)):
        if txt1[i] == txt2[i]:
            counter += 1
    if counter == len(txt1)-1:
        return True
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))