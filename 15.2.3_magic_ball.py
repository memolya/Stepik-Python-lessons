from random import *

answers = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай',
'Предрешено',	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет',
'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать', 'По моим данным - нет',
'Определённо да', 'Знаки говорят - да',	'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
# print(len(answers))

def greeting():
    print('Привет, Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Введи свое имя: ')
    print('Привет ' + name)

def magic_ball():
    question = input('Введи свой вопрос: ')
    num = randrange(21)
    print(answers[num])
    more()

def more():
    print('Играть дальше? да/нет ')
    answer = input()
    if answer.lower() == 'да':
        magic_ball()

    else:
        print('Возвращайся, если возникнут вопросы!')
        exit() #interrupt the whole code if 'no' enters

greeting()
magic_ball()
