import random


def play():
    print_opening_message()
    secret_word = load_secret_word()
    user_word = initialize_user_word(secret_word)

    errors = 0
    attempts = 7
    corrected_word = False
    hanged = False

    while not corrected_word and not hanged:
        user_guess = ask_user_guess()

        if user_guess in user_word:
            print('You already typed it! Try again!\n')
            continue

        if user_guess in secret_word:
            match_right_guess(secret_word, user_guess, user_word)
            print('Yep!! A hit! Your word: {}\n'.format(user_word))
        else:
            errors += 1
            draw_gallows(errors)

        hanged = errors == attempts
        corrected_word = '_' not in user_word

    print_endgame_messages(secret_word, corrected_word, hanged)


def print_opening_message():
    print("\n*********************************")
    print("***    Welcome to Hangman!    ***")
    print("*********************************\n")


def load_secret_word(file_name='words.txt', from_line=0):
    file = open(file_name, 'r')
    list_of_words = [word.strip() for word in file]
    file.close()

    # It also can be this way:
    # with open('words.txt') as file:
    #   list_of_words = [word.strip() for word in file]

    number = random.randrange(from_line, len(list_of_words))
    secret_word = list_of_words[number].upper()
    return secret_word


def initialize_user_word(secret_word):
    user_word = ['_' for l in secret_word]
    print('Try to find out the word: {}\n'.format(user_word))
    return user_word


def ask_user_guess():
    answer = input("Type a letter: ")
    answer = answer.strip().upper()
    return answer


def match_right_guess(secret_word, user_guess, user_word):
    index = 0
    for l in secret_word:
        if l == user_guess:
            user_word[index] = user_guess
        index += 1
    return user_word


def print_endgame_messages(secret_word, corrected_word, hanged):
    if hanged:
        print_loser_message(secret_word)
    if corrected_word:
        print_win_message()
    print("********** Game over! ***********")


def print_loser_message(secret_word):
    print("!!! YOU WAS HANGED !!!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_win_message():
    print("*** Congratulations! You win! ***")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
