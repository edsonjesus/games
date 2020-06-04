
def jogar():
    print("*********************************")
    print("***    Welcome to Hangman!    ***")
    print("*********************************")

    secret_word = "banana";
    hit = False
    hanged = False

    while(not hit and not hanged):
        answer = input("Type a letter: ")
        answer = answer.strip()
        index = 0
        for l in secret_word.lower():
            if l == answer.lower():
                print("Letter {} found at position {}".format(answer, index))
            index = index+1
        hit = True
    print("********** Game over! ***********")

if (__name__ == "__main__"):
    jogar()