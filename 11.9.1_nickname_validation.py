text = input()
available = list('abcdefghijklmnopqrstuvwxyz0123456789')
Flag = True

for _ in range(len(text)):
    if text[0] != '@':
        Flag = False
    elif len(text) < 5 or len(text) > 15:
        Flag = False
    for i in range(1, len(text)):
        if text[i] not in available:
            Flag = False

if Flag == False:
    print('Incorrect')
else:
    print('Correct')

# s = input()
#
# if (
#     s.startswith('@')
#     and 5 <= len(s) <= 15
#     and s[1:].isalnum()
#     and s == s.lower()
# ):
#     print('Correct')
# else:
#     print('Incorrect')