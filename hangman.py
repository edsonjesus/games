import random

def jogar():
    print("\n*********************************")
    print("***    Welcome to Hangman!    ***")
    print("*********************************\n")

    file = open('words.txt', 'r')
    list_of_words = [word.strip() for word in file]
    file.close()
    # with open('words.txt') as file:
    #   list_of_words = [word.strip() for word in file]

    number = random.randrange(0, len(list_of_words))

    secret_word = list_of_words[number].upper()
    user_word = ['_' for l in secret_word]
    errors = 0
    attempts = 6

    print('Word: {}\n'.format(user_word))

    while True:
        answer = input("Type a letter: ")
        answer = answer.strip().upper()

        if answer in user_word:
            print('You already typed it! Try again!\n')
            continue

        if answer in secret_word:
            index = 0
            for l in secret_word:
                if l == answer:
                    user_word[index] = answer
                index += 1
            print('Yep!! Your word: {}\n'.format(user_word))
        else:
            errors += 1
            print('You missed! There are {} attempts left.'.format(attempts-errors))

        if errors == attempts:
            print("\n***** You lost! Try again! ******")
            break

        if '_' not in user_word:
            print("*** Congratulations! You win! ***")
            break
    print("********** Game over! ***********")

if (__name__ == "__main__"):
    jogar()