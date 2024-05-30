def is_password_good(password):
    checks = 0

    for i in range(len(password)):
        if password[i].islower():
            checks += 1
            break
        else:
            continue

    for z in range(len(password)):
        if password[z].isupper():
            checks += 1
            break
        else:
            continue

    for x in range(len(password)):
        if password[x].isdigit():
            checks += 1
            break
        else:
            continue

    if len(password) >= 8 and checks == 3:
        return True
    else:
        return False


text = input()

print(is_password_good(text))

# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3 - можно вернуть сразу 3 флага, если один false - то остальные тоже false
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))