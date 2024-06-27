from random import *

def get_word(a_list):
    return choice(a_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    print(stages[tries])


def is_valid_letter(letter):
    return ord("А") <= ord(letter) <= ord("Я")


def is_valid_word(word):
    for c in word:
        if not is_valid_letter(c):
            return False
    else:
        return True


def guess_word(word):
    while True:
        print()
        guess = input(f"Введите букву или слово из {len(word)} букв: ").strip().upper()
        if len(guess) == 1 and not is_valid_letter(guess):
            print("Такой буквы нет в русском языке.")
            continue
        elif len(guess) == len(word) and not is_valid_word(guess):
            print("Такого слова в русском языке нет.")
            continue
        elif len(guess) != 1 and len(guess) != len(word):
            print(f"Слово должно состоять из {len(word)} букв.")
            continue
        else:
            return guess


def play(word):
    print("Давайте играть в угадайку слов!")

    word_completion = "_" * len(
        word
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    display_hangman(tries)

    while tries > 0:
        print("Загаданное слово:", word_completion)
        maybe = guess_word(word)

        if len(maybe) == len(word):
            if maybe in guessed_words:
                print("Вы уже вводили это слово.")
                continue

            guessed_words.append(maybe)

        if len(maybe) == 1:
            if maybe in guessed_letters:
                print("Вы уже вводили эту букву.")
                continue

            guessed_letters.append(maybe)
            word_completion = ""

            for c in word:
                if c in guessed_letters:
                    word_completion += c
                else:
                    word_completion += "_"

        if maybe not in word:
            tries -= 1
            display_hangman(tries)
            continue

        if maybe == word or word_completion == word:
            print("Поздравляем, вы угадали слово! Вы победили!")
            break

    else:
        print("GAME OVER")


word_list = [
    "яблоко",
    "груша",
    "персик",
    "банан",
    "гранат",
    "вишня",
    "слива",
    "малина",
    "клубника",
    "черешня",
    "виноград",
    "манго",
]
word = get_word(word_list)

play(word)