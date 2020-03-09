#Importing GUI module
from tkinter import *
#Importing number module for dropzeros function
import decimal
  
#Function that drops trailing zeros, all from https://stackoverflow.com/questions/11227620/drop-trailing-zeros-from-decimal/44961532#44961532
def dropzeros(number):
    mynum = decimal.Decimal(number).normalize()
    # e.g 22000 --> Decimal('2.2E+4')
    return mynum.__trunc__() if not mynum % 1 else float(mynum)

# function to calculate math function when button is clicked
def calculate() :

    #Tries for error from divide by 0
    try:
        #Tries for error from inputing something other than a number
        try:
            #Grabs numbers and operator from text boxes and assigns then to a variable
            number1 = float(firstNumber.get())
            number2 = float(secondNumber.get())
            operation = operator.get()
            
            #Addition
            if operation == '+':
                equals = number1 + number2
                resultText.set('{} + {} = {}'.format(dropzeros(number1), dropzeros(number2), dropzeros(equals)))
                
            #Subtraction
            elif operation == '-':
                equals = number1 - number2
                resultText.set('{} - {} = {}'.format(dropzeros(number1), dropzeros(number2), dropzeros(equals)))
                
            #Multiplication
            elif operation == '*':
                equals = number1 * number2
                resultText.set('{} * {} = {}'.format(dropzeros(number1), dropzeros(number2), dropzeros(equals)))

            #Division
            elif operation == '/':
                equals = number1 / number2
                resultText.set('{} / {} = {}'.format(dropzeros(number1), dropzeros(number2), dropzeros(equals)))

            #Power
            elif operation == '^':
                equals = number1 ** number2
                resultText.set('{} ^ {} = {}'.format(dropzeros(number1), dropzeros(number2), dropzeros(equals)))


            #If operator doesn't match what is given
            else:
                resultText.set("Invalid Operator\nPlease use one of the\nfollowing:\n+ - * / ^")
        #Catches error from inputing letter instead of number
        except ValueError:
            resultText.set("Invalid Number")
    #Catches error from divide by 0
    except ZeroDivisionError:
        resultText.set("Can't divide by 0")


      
  
# Driver Code 
if __name__ == "__main__" : 
  
    # Create a GUI window 
    gui = Tk() 
  
    # Set the background colour of GUI window   
    gui.configure(background = "light green") 
  
    # set the name of tkinter GUI window  
    gui.title("Calculator") 

    # First number label 
    firstNumberLabel = Label(gui, text = "Number 1", bg = "light green") 
  
    # Second number label 
    secondNumberLabel = Label(gui, text = "Number 2", bg = "light green") 
  
    # Operator label 
    operatorLabel = Label(gui, text = "Operator (+ - * / ^)", bg = "light green") 

    # Result label, asigns label text to a variable so what ever the variable is is what is displayed
    resultText = StringVar()
    result = Label(gui, textvariable = resultText, bg = "light green") 

    # Label that adds some padding to the right side of the window
    padding = Label(gui, text = "    ", bg = "light green")
  
  
    # Calculate button that runs the calculate function when ran
    btnCalculate = Button(gui, text = "Calculate", fg = "Black", bg = "Red", command = calculate) 
  
    # Text box entries
    firstNumber = Entry(gui) 
    secondNumber = Entry(gui) 
    operator = Entry(gui) 
      

  
  
    # grid method used for placing widgets at set places like in a grid
    
    #First number label and text box
    firstNumberLabel.grid(row = 1, column = 0) 
    firstNumber.grid(row = 1, column = 1) 
    
    #Operator label and text box
    operatorLabel.grid(row = 2, column = 0) 
    operator.grid(row = 2, column = 1) 

    #Second number label and text box
    secondNumberLabel.grid(row = 3, column = 0) 
    secondNumber.grid(row = 3, column = 1) 
   
    #Calculate button
    btnCalculate.grid(row = 4, column = 1) 

    #Result label
    result.grid(row = 5, column = 1) 

    #Padding
    padding.grid(row = 4, column = 2) 
    

  
    # Start the GUI 
    gui.mainloop()     

