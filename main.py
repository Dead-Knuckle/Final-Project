# Importing requried modules
import os
import time
import maskpass
import numpy
from termcolor import cprint
from cryptography.fernet import Fernet
from fileBeef import *
# Different OS use different commands to clear the screen, linux:clear win:cls
CLEAR_SCREEN = 'cls'
TIMEOUT = 10
# Defining The Correct Password and The Password Attempt amount
correct_password = 'password1'  # Need to remove.  Not used anymore.
PASSWORD_ATTEMPT = 3
# Clearing the Screen
os.system(CLEAR_SCREEN)

# Main app begins here
while True:

    # Checking if the user trys to bypass the password with a keyboard interrupt
    try:

        # Getting the users password input with a security mask
        cprint('[*]Password: ', 'blue', end="")
        password_input = maskpass.askpass(prompt="", mask="*")

        # Checking if password is the correct password, if so we break from loop
        if checkUser(password_input):
            # math_equation_problem = ['1 + 2', '5 * 2',
            #                          '3 - 2 - 1', '25/5/ 5', '23/5']
                cprint(f'[+]Welcome User', 'green')
                f = open("quiz.txt", "r",  encoding='utf-8-sig')
                quizFile =f.readlines()
                print(f.read())
                for math_equation in quizFile:
                    if math_equation =="\n":
                        continue
                    cprint(f'[*]Problem: {math_equation}', 'blue')
                    cprint(f'[+]Results:{mathResults(firgureMath(math_equation), math_equation)}\n\n', 'green')


        # Else, we subtract one from their attempts , and print it to the user
        else:
            PASSWORD_ATTEMPT -= 1
            cprint(
                f'[-] Wrong password, you have {PASSWORD_ATTEMPT} remaining', 'red')

        # If the user has run out of password attempts then we clear the screen and quit the program
        if PASSWORD_ATTEMPT == 0:
            os.system(CLEAR_SCREEN)
            cprint('[-] You have run out of password attempts.\n', 'red')
            for i in range(TIMEOUT):
                cprint(f'[-] Locked for {TIMEOUT-i} seconds.', 'yellow')
                time.sleep(1)
            cprint('[-] Resetting password atempts post lockout', 'yellow')
            PASSWORD_ATTEMPT = 3
            # exit()

    except KeyboardInterrupt:

        # A taunting message is displayed if the user tries to use KeyboardInterrupt, and the loop continues
        cprint("\n[!] Nice try, it won't be that easy", 'yellow')
        continue
