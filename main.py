# Importing requried modules
import json
import requests
import maskpass
import os
from termcolor import cprint

# Different OS use different commands to clear the screen, linux:clear win:cls
clear_screen = 'cls'

# Defining The Correct Password and The Password Attempt amount
correct_password = 'password1'
password_attempt = 11
API_KEY = 'K83002919388957'

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


def ocr_space_file(filename, overlay=True, api_key=API_KEY, language='eng'):
    """Function to use OCR Space's API"""
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f}, data=payload)
    m = r.content.decode()
    jsonstr = json.loads(m)
    print(jsonstr["ParsedResults"][0]["ParsedText"])


ocr_space_file(filename='exam.jpg', language='eng')
