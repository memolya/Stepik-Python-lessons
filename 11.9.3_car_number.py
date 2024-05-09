number = input()
correct_letters = 'АВЕКМНОРСТУХ'

if (
        9 <= len(number) <= 10
        and number[0] in correct_letters
        and number[4] in correct_letters
        and number[5] in correct_letters

        and number[1].isdigit()
        and number[2].isdigit()
        and number[3].isdigit()

        and number[6] == '_'

        and number[7].isdigit()
        and number[8].isdigit()
        and number[-1].isdigit()
):
    print('YES')
else:
    print('NO')

# s = input()
# flag = 'NO'
# correct_letters = 'АВЕКМНОРСТУХ'
#
# if 9 <= len(s) <= 10:
#     letters = s[0] + s[4:6]
#     digits = s[1:4] + s[7:]
#     underscore = s[6]
#
#     if digits.isdigit() and underscore == "_":
#         flag = 'YES'
#
#     for c in letters:
#         if c not in correct_letters:
#             flag = 'NO'
#
# print(flag)