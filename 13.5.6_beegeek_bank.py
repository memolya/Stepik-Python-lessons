def is_valid_password(password):
    flag1 = False
    flag2 = False
    flag3 = False

    #no more than 3 instances
    if len(psw) != 3:
        return False

    # palyndrome
    if str(a[:]) == str(a[::-1]):
        flag1 = True

    # prime
    if b == 1:
        return False

    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            flag2 = False
            break
        else:
            flag2 = True

    # even
    if c % 2 == 0:
        flag3 = True

    return flag1 and flag2 and flag3

# считываем данные
psw = input()
psw = psw.split(':')

a, b, c = psw[0], int(psw[1]), int(psw[2])

#debug
# print('a =', a, type(a), 'b =', b, type(b), 'c =', c, type(c))
# print(len(psw))

# вызываем функцию
print(is_valid_password(psw))