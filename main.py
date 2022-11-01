# Importing requried modules
import os
import maskpass
import numpy
from termcolor import cprint
from cryptography.fernet import Fernet

# Different OS use different commands to clear the screen, linux:clear win:cls
CLEAR_SCREEN = 'cls'

# Defining The Correct Password and The Password Attempt amount
PASSWORD_ATTEMPT = 11

# Function to check if the Users password is correct
def check_user(passwd):
    """Check passwords in file for match"""
    # Opening the file that contains username, encrypted password, and keys in a Read Only state.
    passwdfile = open('./passwd.txt', 'r', encoding='utf-8')
    # Use a for loop to itterate through each line in the password file.
    for line in passwdfile:
        # Using a colon : to sperate username, encrypted password and key in the password file.
        # Splitting each line on that delimiter.
        passwordlineread = line.split(':')
        # Reading in the key for the current line
        fernet = Fernet(passwordlineread[2].encode())
        # Will return True if the decrypted password and the password the user put in match.
        if fernet.decrypt(passwordlineread[1].encode()) == passwd.encode():
            return True
    # For security, we return False if the bool expression never matches True.
    return False


# Clearing the Screen
os.system(CLEAR_SCREEN)

# Defining password loop
while True:

    # Checking if the user trys to bypass the password with a keyboard interrupt
    try:

        # Getting the users password input with a security mask
        cprint('[*]Password: ', 'blue', end="")
        password_input = maskpass.askpass(prompt="", mask="*")


        # Checking if password is the correct password, if so we break from loop
        if check_user(password_input):
            break

        # Else, we subtract one from their attempts , and print it to the user
        PASSWORD_ATTEMPT -= 1
        cprint(
            f'[-] Wrong password, you have {PASSWORD_ATTEMPT} remaining', 'red')

        # If the user has run out of password attempts then we clear the screen and quit the program
        if PASSWORD_ATTEMPT == 0:
            os.system(CLEAR_SCREEN)
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