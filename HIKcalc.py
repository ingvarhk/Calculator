import math

print("WELCOME TO HIKcalc!!")
print("-----------------------------------------------")
print("See commands and examples by typing 'help'")
print("")
result = 0
currentMethod = "addition"

def addition(num1, num2):
    returnSum = 0
    returnSum = num1 + num2

    return returnSum

def subtraction(num1, num2):
    returnSum = 0
    returnSum = num1 - num2

    return returnSum

def multiplication(num1, num2):
    returnSum = 0
    returnSum = num1 * num2

    return returnSum

def divison(num1, num2):
    returnSum = 0
    returnSum = num1 / num2

    return returnSum

def sqareroot(num1):
    returnSum = math.sqrt(num1)
    return returnSum

def power(num1, num2):
    returnSum = math.pow(num1, num2)
    return returnSum

def userHelp():
    print("""COMMANDS
# plus -- Plus two numbers with each other
# min -- Minus a number with a number
# mult -- Multiply numbers
# divd -- Divide numbers
# sqrt -- Get sqareroot of number
# pow -- Get det power of number

EXAMPLES
# Input: 'plus 40 5'
# Output: '45'
#
# Input: 'divd 34 10'
# Output: '3.4'
#
# Input: 'pow 4 2'
# Output: '16'

DOCUMENTATION
""")


while True:
    userInput = input("> ")
    
    if userInput == "help":
        userHelp()





