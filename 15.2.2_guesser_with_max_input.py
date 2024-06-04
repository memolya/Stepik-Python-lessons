from random import *


        return True
    return False


def is_valid(num):
    if num.isdigit() and 0 < int(num) <= n:
        return True
    return False


def guess_number():

    print('Компьютер загадал число от 1 до ' + str(n) + ' Попробуйте угадать!')
    attempts = 0

    while True:
        input_guess = input("Введите вашу догадку: ")

        if not is_valid(input_guess):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue

        guess = int(input_guess)
        attempts += 1

        if guess < random_num:
            print("Загаданное число больше вашей догадки.")
        elif guess > random_num:
            print("Загаданное число меньше вашей догадки.")
        else:
            print(
                f"Поздравляем! Вы угадали число {random_num} за {attempts} попыток!", end = '\n'
                'Играть дальше? да/нет ')

            answer = input()
            if answer == 'да':
                guess_number()
                print('Играть дальше? да/нет ')

            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

print('Введите целое число для определения максимального возможного числа: ')
n = int(input())
if n.isdigit() and int(n) > 0:
    random_num = randint(1, n + 1)

guess_number()

