phone_number = input()
def type_check():
    if digits.isdigit() and score in '---':
        print('YES')
    else:
        print('NO')

if len(phone_number) == 12:
    digits = phone_number[0:3] + phone_number[4:7] + phone_number[8:12]
    score = phone_number[-5] + phone_number[-9]
    type_check()


elif len(phone_number) == 14 and phone_number[0] == '7':
    digits = phone_number[0] + phone_number[2:5] + phone_number[6:9] + phone_number[10:14]
    score = phone_number[1] + phone_number[5] + phone_number[9]
    type_check()

else:
    print('NO')