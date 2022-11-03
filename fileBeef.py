import os
import time
import maskpass
import numpy
from termcolor import cprint
from cryptography.fernet import Fernet
import smtplib

def checkUser(passwd):
    # Opening the file that contains username, encrypted password, and keys in a Read Only state.
    passwdFile = open('./passwd.txt', 'r', encoding='utf-8')
    # Use a for loop to itterate through each line in the password file.
    for line in passwdFile:
        # Using a colon : to sperate username, encrypted password and key in the password file.
        # Splitting each line on that delimiter.
        passwordLineRead = line.split(':')
        # Reading in the key for the current line
        fernet = Fernet(passwordLineRead[2].encode())
        # Will return True if the decrypted password and the password the user put in match.
        if fernet.decrypt(passwordLineRead[1].encode()) == passwd.encode():
            return True
    # For security, we return False if the bool expression never matches True.
    return False



def firgureMath(mathEquation):
    """A simple way to firgure what math equal needs to be done"""
    mathOper = ['+', '-', '/', '*']
    for index in mathOper:
        if index in mathEquation:
            return index


def mathResults(operator: str, mathEquation: str):
    mathEquation = mathEquation.split(operator)
    mathEquation = [int(x) for x in mathEquation]
    if operator == '+':
        return sum(mathEquation)
    elif operator == '*':
        return numpy.prod(mathEquation)
    elif operator == '-':
        accumulate = mathEquation[0]
        for i in range(1,len(mathEquation)):
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

def sendMail(gmail_user, gmail_password, to, subject, body):
    sent_from = gmail_user
    message = 'Subject: {}\n\n{}'.format(subject, body)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, message)
        smtp_server.close()
        return True
    except Exception as ex:
        return ex