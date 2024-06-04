# объявление функции
def edges(text):
    if txt[0] == "(" and txt[-1] == ")":
        return True
    else:
        return False

def all_brackets(text):
    counter = 0
    for i in range(len(txt)):
        if txt[i] == '(':
            counter += 1
        else:
            counter -= 1

        if counter < 0:
            return False

    if counter == 0:
        return True
    else:
        return False


def is_correct_bracket(text):
    return edges(txt) and all_brackets(txt)


# считываем данные
txt = input()

# # вызываем функцию
print(is_correct_bracket(txt))

#
# # объявление функции
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#
#     return text == ""
# 
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))