import random, time

#Game Function
def GuessTheNumber():
    #Initial
    print("Please guess a number from 1 to 1000")
    guesses = 1
    number = random.randrange(1, 1001)
    print("Guess {}".format(guesses))
    guess = int(input())
    

    while number != guess:
        if guess > number:
            print("Your guess is high, please try again")
        else:
            print("Your guess is low, please try again")
        print("Guess {}".format(guesses))
        guess = int(input())
        guesses += 1

    print("Congratulations, you guessed the number, it was: {}. It took you {} guesses!".format(number, guesses))
    again()

def again():
    #Asks for input
    askAgain = input('''
Do you want to play again?
Please type Y for YES or N for NO.
    ''')
    #If Y, runs math function again
    if askAgain.upper() == 'Y':
        calculate()
    #If N, ends program
    elif askAgain.upper() == 'N':
        print('\nSee you later.\n')
        #Leaves time before program closes
        time.sleep(4)
    #If Y or N not inputed asks again
    else:
        again()
    
GuessTheNumber()
