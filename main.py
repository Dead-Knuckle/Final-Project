# Importing requried modules
import math
from cv2 import accumulate
import maskpass, os, numpy
from termcolor import cprint

# Different OS use different commands to clear the screen, linux:clear win:cls
clear_screen = 'cls'

# Defining The Correct Password and The Password Attempt amount
correct_password = 'password1'
password_attempt = 11


# Clearing the Screen
os.system(clear_screen)

# Defining password loop
while True:

    # Checking if the user trys to bypass the password with a keyboard interrupt
    try:

        # Getting the users password input with a security mask
        cprint('[*]Password: ', 'blue', end="")
        password_input = maskpass.askpass(prompt="", mask="*")

        # Checking if password is the correct password, if so we break from loop
        if password_input == correct_password:
            break

        # Else, we subtract one from their attempts , and print it to the user
        password_attempt -= 1
        cprint(
            f'[-] Wrong password, you have {password_attempt} remaining', 'red')

        # If the user has run out of password attempts then we clear the screen and quit the program
        if password_attempt == 0:
            os.system(clear_screen)
            cprint('[-] You have run out of password attempt, goodbye', 'red')
            exit()

    except KeyboardInterrupt:

        # A taunting message is displayed if the user tries to use KeyboardInterrupt, and the loop continues
        cprint("[!] Nice try, it won't be that easy", 'red')
        continue

def firgureMath(mathEquation):
    """A simple way to firgure what math equal needs to be done"""
    mathOper = ['+', '-', '/', '*']
    for index in mathOper:
        if index in mathEquation:
            return index 

def mathResults(operator : str, mathEquation : str): 
    mathEquation=mathEquation.split(operator)
    mathEquation = [ int(x) for x in mathEquation ]
    if operator == '+':
        return sum(mathEquation)
    elif operator == '*':
        return numpy.prod(mathEquation)
    elif operator == '-':
        accumulate = 0
        for i in mathEquation:
            accumulate -= i
        return accumulate
    elif operator == '/':
        
        accumulate = mathEquation[0] / mathEquation[1]
        if len(mathEquation) == 2:
            return accumulate
        else:
            for i in range(2, len(mathEquation)):
                accumulate /= mathEquation[i]
            return accumulate
math_equation_add = '1 + 2'
math_equation_product = '5 * 2'
math_equation_subtraction = '3 - 2 - 1'
math_equation_division = '25 / 5'
print(mathResults(firgureMath(math_equation_add), math_equation_add))
print(mathResults(firgureMath(math_equation_product), math_equation_product))
print(mathResults(firgureMath(math_equation_subtraction), math_equation_subtraction))
print(mathResults(firgureMath(math_equation_division), math_equation_division))