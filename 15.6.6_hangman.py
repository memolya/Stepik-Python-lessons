from random import *
global word_list
word_list = ['шлепа', 'пепе', 'чонгус', 'гигачад', 'сигма', 'альфа', 'форчан', 'двач', 'папуг']


def get_random_word():
    return word_list[randint(0, len(word_list) - 1)].upper()

def display_hangman(tries):
    line_1 = "--------"
    line_2 = "|      |"
    line_3 = "|       "
    line_4 = "|       "
    line_5 = "|       "
    line_6 = "|       "
    line_7 = "-       "

    if tries < 6:
        line_3 = "|      O"
    if tries < 5:
        line_4 = "|      |"
        line_5 = "|      |"
    if tries < 4:
        line_4 = "|     \\|"
    if tries < 3:
        line_4 = "|     \\|/"
    if tries < 2:
        line_6 = "|     / "
    if tries < 1:
        line_6 = "|     / \\"

    print(line_1, line_2, line_3, line_4, line_5, line_6, line_7, sep="\n")

get_random_word()