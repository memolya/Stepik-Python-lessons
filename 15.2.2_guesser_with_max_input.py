from random import *

def is_valid(num):
    if num.isdigit() and 0 < int(num) <= max_num:
        return True
    return False

def more():
    print('Играть дальше? да/нет ')
    answer = input()
    if answer == 'да':
        guess_number()

    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        exit() #interrupt the whole code if 'no' enters

def guess_number():
    global max_num
    max_num = int(input('Введите максимальное возможное число: '))
    random_num = randint(1, max_num)
    print('Компьютер загадал число от 1 до ' + str(max_num) + '. ' + 'Попробуйте угадать!')
    attempts = 0

    while True:
        input_guess = input("Введите вашу догадку: ")

        if not is_valid(input_guess):
            print('А может быть все-таки введем целое число от 1 до ' + str(max_num) + '?')
            continue

        guess = int(input_guess)
        attempts += 1

        if guess < random_num:
            print("Загаданное число больше вашей догадки.")
        elif guess > random_num:
            print("Загаданное число меньше вашей догадки.")
        else:
            print(f"Поздравляем! Вы угадали число {random_num} за {attempts} попыток!", end = '\n')
            more()

guess_number()