from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
dubious_chars = 'il1Lo0O'

chars = '' #all symbols that can exist in a generated password
password = ''
passwords = []

def password_rules():
    global chars
    global lowercase_letters
    global uppercase_letters
    global punctuation
    global digits
    global dubious_chars

    while True:
        print('Включить в пароль числа 0-9?')
        answer = input()

        if answer.lower() == 'да':
            chars += digits

        print('Включить в пароль прописные буквы A-Z?')
        answer = input()
        if answer.lower() == 'да':
            chars += uppercase_letters

        print('Включить в пароль строчные буквы a-z?')
        answer = input()
        if answer.lower() == 'да':
            chars += lowercase_letters

        print('Включить в пароль специальные символы?')
        answer = input()
        if answer.lower() == 'да':
            chars += punctuation

        print('Исключить из пароля неоднозначные символы "il1Lo0O"?')
        answer = input()
        if answer.lower() == 'да':
            if dubious_chars in chars:
                chars = chars.replace(dubious_chars, '')
        else:
            break
        break

def pass_gen():
    global password
    global number
    #for amount of passwords required
    while number != 0:
        #for each password
        for z in range(pw_length):
            z = choice(chars)
            password += z
        passwords.append(password)
        number -= 1
        password = ''

    print('Ваши пароли:')
    print(*passwords, sep = '\n')

number = int(input('Укажите количество требуемых паролей: '))
pw_length = int(input('Укажите длину требуемых паролей: '))
print('Вы запросили ' + str(number) + ' паролей ' + 'длиной ' + str(pw_length) + ' символов.')

password_rules()
pass_gen()


