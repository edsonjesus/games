
def jogar():
    print("\n*********************************")
    print("***    Welcome to Hangman!    ***")
    print("*********************************\n")

    secret_word = "banana"
    user_word = ['_', '_', '_', '_', '_', '_']
    hit = False
    hanged = False

    print('Word: {}\n'.format(user_word))
    while(not hit and not hanged):
        answer = input("Type a letter: ")
        answer = answer.strip()
        index = 0
        for l in secret_word.lower():
            if l == answer.lower():
                user_word[index] = answer
            index = index+1
        print('Your word: {}\n'.format(user_word))
        if '_' not in user_word:
            hit = True
            print("*** Congratulations! You win! ***")
    print("********** Game over! ***********")

if (__name__ == "__main__"):
    jogar()