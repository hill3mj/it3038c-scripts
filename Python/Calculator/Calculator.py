#Needed to wait a few seconds before program closes
import time

#Math Function
def calculate():
    operation = input('''Please type in the math osperation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division\n''')

    #Gather inputs
    #Tries for error from divide by 0
    try:
        #Tries for error from inputing letter instead of number
        try:
            number1 = int(input('\nEnter your first number: '))
            number2 = int(input('Enter your second number: '))
            #Addition
            if operation == '+':
                print('\n{} + {} = '.format(number1, number2))
                print(number1 + number2)
            #Subtraction
            elif operation == '-':
                print('\n{} - {} = '.format(number1, number2))
                print(number1 - number2)
            #Multiplication
            elif operation == '*':
                print('\n{} * {} = '.format(number1, number2))
                print(number1 * number2)
            #Division
            elif operation == '/':
                print('\n{} / {} = '.format(number1, number2))
                print(number1 / number2)

            #If input doesn't match
            else:
                print('\nYou have not typed a valid operator, please run the program again.')
        #Catches error from inputing letter instead of number and goes straight into again()
        except ValueError:
            print('\nYou have not typed a valid number, please run the program again.')
    #Catches error from divide by 0 and goes straight into again()
    except ZeroDivisionError:
        print('You have divided by 0, which does not exist. Please run the program again')
        #Runs function again
    again()
    
#Function to run math function again
def again():
    #Asks for input
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
    ''')
    #If Y, runs math function again
    if calc_again.upper() == 'Y':
        calculate()
    #If N, ends program
    elif calc_again.upper() == 'N':
        print('\nSee you later.\n')
        #Leaves time before program closes
        time.sleep(4)
    #If Y or N not inputed asks again
    else:
        again()

###### RUNNING CODE ######
#Welcomes user
print('''
* * * * *  Welcome to Integer Calculator  * * * * *

''')
#Begins loop until user exits
calculate()
