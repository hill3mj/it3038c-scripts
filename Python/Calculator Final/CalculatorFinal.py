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
        try:
            #Grabs numbers and operator from privious inputs and assigns then to a variable
            number1 = float(numberTwo.get())
            number2 = float(numberOne.get())
            operationSign = operation.get()
            
            #Addition
            if operationSign == '+':
                equals = number1 + number2
                numberOne.set(equals)
                
            #Subtraction
            elif operationSign == '-':
                equals = number1 - number2
                numberOne.set(equals)
                               
            #Multiplication
            elif operationSign == '*':
                equals = number1 * number2
                numberOne.set(equals)
                
            #Division
            elif operationSign == '/':
                equals = number1 / number2
                numberOne.set(equals)
                
            #Error display if something goes terribly wrong
            else:
                numberOne.set("ERROR")
                
        #Catches if only one number is clicked
        except ValueError:
            numberOne.set("Enter Second Number and Try Again")
            resetStartFlag.set("f")

    #Catches error from divide by 0
    except ZeroDivisionError:
        numberOne.set("Can't divide by 0")
        resetStartFlag.set("f")

    #Resets operation and sets flag to restart
    operation.set("")
    resetStartFlag.set("f")

#Number button functons, will only comment this first one
def press1():
    #If the reset flag is f then it erase what ever is in the display when the number is clicked
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    #Assigns the label to a varible
    number = numberOne.get()
    #Adds another number onto the label
    number = number + "1"
    #Assigns the variable to the label
    numberOne.set(number)

def press2():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "2"
    numberOne.set(number)

def press3():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "3"
    numberOne.set(number)

def press4():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "4"
    numberOne.set(number)

def press5():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "5"
    numberOne.set(number)

def press6():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "6"
    numberOne.set(number)

def press7():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "7"
    numberOne.set(number)

def press8():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "8"
    numberOne.set(number)

def press9():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "9"
    numberOne.set(number)

def press0():
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    number = numberOne.get()
    number = number + "0"
    numberOne.set(number)

#Operation Functions, will only comment first one
def pressAdd():
    #if there is an operation saved (when tring to calculate with more than 2 numbers), spits a message and resets
    if operation.get() != "":
        numberOne.set("Please use two numbers at a time")
        numberOne.set("")
        numberTwo.set("")
    #If no operation saved, then operation is saved and number in label is pushed into another variable and the label is reset for the second variable
    else:
        operation.set('+')
        number = numberOne.get()
        numberTwo.set(number)
        numberOne.set("")
   
def pressMinus():
    if operation.get() != "":
        numberOne.set("Please use two numbers at a time")
        numberOne.set("")
        numberTwo.set("")
    else:
        operation.set('-')
        number = numberOne.get()
        numberTwo.set(number)
        numberOne.set("")

def pressTimes():
    if operation.get() != "":
        numberOne.set("Please use two numbers at a time")
        numberOne.set("")
        numberTwo.set("")
    else:
        operation.set('*')
        number = numberOne.get()
        numberTwo.set(number)
        numberOne.set("")


def pressDivide():
    if operation.get() != "":
        numberOne.set("Please use two numbers at a time")
        numberOne.set("")
        numberTwo.set("")
    else:
        operation.set('/')
        number = numberOne.get()
        numberTwo.set(number)
        numberOne.set("")

#When Decimal is clicked
def pressDecimal():
    #If calculator is recently reset, then this won't mess things up
    if resetStartFlag.get() == "f":
        numberOne.set("0")
        numberTwo.set("")
        resetStartFlag.set("t")
    #if there is a . already then it will not do anything
    if numberOne.get().find(".") < 0:
        number = numberOne.get()
        number = number + "."
        numberOne.set(number)

#Negative/Positive Toggle
def pressNegative():
    #So it doesn't mess up if recently reset.
    if resetStartFlag.get() == "f":
        numberOne.set("")
        numberTwo.set("")
        resetStartFlag.set("t")
    #The toggle, if positive will assign it to negative and vise versa
    if numberOne.get().find("-") < 0:
        number = numberOne.get()
        number = "-" + number
        numberOne.set(number)
    else:
        number.replace("-", "")

# Driver Code 
if __name__ == "__main__" : 
  
    # Create a GUI window 
    gui = Tk() 
  
    # Set the background colour of GUI window   
    gui.configure(background = "light green") 
  
    # set the name of tkinter GUI window  
    gui.title("Calculator") 

    #Global Variables that I use
    numberOne = StringVar()
    numberTwo = StringVar()
    total = StringVar()
    operation = StringVar()
    resetStartFlag = StringVar()
    #Assigning some variable
    numberOne.set("")
    numberTwo.set("0")
    resetStartFlag.set("f")
    operation.set("")
    total.set("0")

    #Creating output label
    outputLabel = Label(gui, textvariable = numberOne, bg = "light green") 

    # Creating buttons
    btn1 = Button(gui, height = 2, width = 4, text = "1", fg = "Black", bg = "Gray", command = press1)
    btn2 = Button(gui, height = 2, width = 4,text = "2", fg = "Black", bg = "Gray", command = press2)
    btn3 = Button(gui, height = 2, width = 4,text = "3", fg = "Black", bg = "Gray", command = press3)
    btn4 = Button(gui, height = 2, width = 4,text = "4", fg = "Black", bg = "Gray", command = press4)
    btn5 = Button(gui, height = 2, width = 4,text = "5", fg = "Black", bg = "Gray", command = press5)
    btn6 = Button(gui, height = 2, width = 4,text = "6", fg = "Black", bg = "Gray", command = press6)
    btn7 = Button(gui, height = 2, width = 4,text = "7", fg = "Black", bg = "Gray", command = press7)
    btn8 = Button(gui, height = 2, width = 4,text = "8", fg = "Black", bg = "Gray", command = press8)
    btn9 = Button(gui, height = 2, width = 4,text = "9", fg = "Black", bg = "Gray", command = press9)
    btn0 = Button(gui, height = 2, width = 4,text = "0", fg = "Black", bg = "Gray", command = press0)
    btnAdd = Button(gui, height = 2, width = 4,text = "+", fg = "Black", bg = "Gray", command = pressAdd)
    btnEquals = Button(gui, height = 2, width = 4,text = "=", fg = "Black", bg = "Gray", command = calculate)
    btnMinus = Button(gui, height = 2, width = 4,text = "-", fg = "Black", bg = "Gray", command = pressMinus)
    btnTimes = Button(gui, height = 2, width = 4,text = "*", fg = "Black", bg = "Gray", command = pressTimes)
    btnDivide = Button(gui, height = 2, width = 4,text = "/", fg = "Black", bg = "Gray", command = pressDivide)
    btnDecimal = Button(gui, height = 2, width = 4,text = ".", fg = "Black", bg = "Gray", command = pressDecimal)
    btnNegative = Button(gui, height = 2, width = 4,text = "±", fg = "Black", bg = "Gray", command = pressNegative)

    # grid method used for placing widgets at set places like in a grid
    #Assigning buttons and label to grid
    outputLabel.grid(row = 1, column = 1, columnspan = 5) 
    btn1.grid(row = 4, column = 1)
    btn2.grid(row = 4, column = 2)
    btn3.grid(row = 4, column = 3)
    btn4.grid(row = 3, column = 1)
    btn5.grid(row = 3, column = 2)
    btn6.grid(row = 3, column = 3)
    btn7.grid(row = 2, column = 1)
    btn8.grid(row = 2, column = 2)
    btn9.grid(row = 2, column = 3)
    btn0.grid(row = 5, column = 2)
    btnAdd.grid(row = 4, column = 4)
    btnEquals.grid(row = 5, column = 4)
    btnMinus.grid(row = 3, column = 4)
    btnTimes.grid(row = 2, column = 4)
    btnDivide.grid(row = 3, column = 5)
    btnDecimal.grid(row = 5, column = 3)
    btnNegative.grid(row = 5, column = 1)
  
    # Start the GUI 
    gui.mainloop()     

