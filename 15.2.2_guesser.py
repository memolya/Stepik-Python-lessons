from random import *


def is_valid(num):
    if num.isdigit() and 0 < int(num) < 101:
        return True
    return False


def guess_number():
    random_num = randint(1, 100)
    print("Компьютер загадал число от 1 до 100. Попробуйте угадать!")
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

guess_number()

