#Read number from the keyboard
def readFromKb():
    #try to convert it to an integer
    guess=input("Enter your guess ->")
    return guess

#Check the guess
def checkGuess(guess,answer):
    #If the guess is correct print message else start again
    if guess==answer:
        print("You guessed right")
    else:
        print("You guessed wrong try again")
        main()

def main():
    answer='correct'
    #Setup a list to hold the guesses
    guessList = []
    #Get the guess
    guess = readFromKb()
    #Add the guess to the list of guesses
    guessList.append(guess)
    checkGuess(guess, answer)


main()
