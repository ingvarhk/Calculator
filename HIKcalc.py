import math
import sys
import os

print("Welcome to HIKcalc!!")
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
    print("""
CALCULATOR COMMANDS
# plus -- Plus two numbers with each other. Takes 2 arguments.
# min -- Minus a number with a number. Takes 2 arguments.
# mult -- Multiply numbers. Takes 2 arguments.
# divd -- Divide numbers. Takes 2 arguments.
# sqrt -- Get sqareroot of number. Takes 1 argument.
# pow -- Get det power of number. Takes 2 arguments.
# deci -- End your command with 'deci' followed by how many decimals you want. Default is 2.

EXAMPLES
# Input: 'plus 40 5'
# Output: '45'

# Input: 'divd 243 34 deci 4'
# Output: '7.1471'

# Input: 'pow 4 2'
# Output: '16'

OTHER COMMANDS
# exit -- Exit HIKcalc.
# help -- List of commands and examples.
# clear -- Clear the screen.

SEE MORE
# http://ingvar.hahnkristensen.dk/hikcalc
# https://github.com/HikBit/HIKcalc
""")


#for x in range(0, 1):
while True:
    
    decimals = 2
    userInput = input("> ")
    
    if " deci " in userInput:
        decimalsPosition = userInput.find('deci ') + 5
        decimals = int(userInput[decimalsPosition : ])
        
        deleteDecimals = userInput.find(' deci ')
        
        userInput = userInput.replace(userInput[deleteDecimals : ], '')
        
    if userInput == "help":
        userHelp()
        

#        PLUS
    elif userInput.startswith('plus '):
        userInput = userInput.replace('plus ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 2:
                print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            else:
                i = 0
            
            for number in numbers:      
                if i == 0:
                    num1 = float(number)
                    i =+ 1
                else:
                    num2 = float(number)
            print("RESULT: " + str(round(addition(num1, num2), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            
#        MINUS
    elif userInput.startswith('min '):
        userInput = userInput.replace('min ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 2:
                print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            else:
                i = 0
                
                for number in numbers:      
                    if i == 0:
                        num1 = float(number)
                        i =+ 1
                    else:
                        num2 = float(number)
                print("RESULT: " + str(round(subtraction(num1, num2), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            
#        MULTIPLY
    elif userInput.startswith('mult '):
        userInput = userInput.replace('mult ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 2:

                print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            else:
                i = 0
                
                for number in numbers:      
                    if i == 0:
                        num1 = float(number)
                        i =+ 1
                    else:
                        num2 = float(number)
                print("RESULT: " + str(round(multiplication(num1, num2), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            
#        DIVIDE
    elif userInput.startswith('divd '):
        userInput = userInput.replace('divd ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 2:
                print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            else:
                i = 0
                
                for number in numbers:      
                    if i == 0:
                        num1 = float(number)
                        i =+ 1
                    else:
                        num2 = float(number)
                print("RESULT: " + str(round(divison(num1, num2), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            
#        SQAREROOT
    elif userInput.startswith('sqrt '):
        userInput = userInput.replace('sqrt ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 1:
                print("ERROR: Make sure you are not using any letters. This command can only take 1 argument")
            else:
                i = 0
                
                for number in numbers:      
                    if i == 0:
                        num1 = float(number)
                        i =+ 1
                    else:
                        num2 = float(number)
                print("RESULT: " + str(round(sqareroot(num1), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 1 argument")
            
#        POWER
    elif userInput.startswith('pow '):
        userInput = userInput.replace('pow ', '', 1)
        
        try:
            numbers = userInput.split(' ')
                
            if len(numbers) != 2:
                print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            else:
                i = 0
                
                for number in numbers:      
                    if i == 0:
                        num1 = float(number)
                        i =+ 1
                    else:
                        num2 = float(number)
                print("RESULT: " + str(round(power(num1, num2), decimals)))
        except Exception:
            print("ERROR: Make sure you are not using any letters. This command can only take 2 arguments")
            
    elif userInput == "exit":
        sys.exit()
    
    elif userInput == "clear":
        os.system('cls')
        
    elif userInput == "":
        pass
    
    else:
        print("Not a valid command!!")
        

        





