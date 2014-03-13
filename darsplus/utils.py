from statics import *
import re # Allows regex for E-Mail validation


def validUsername(username):
    """
    Checks if a username's length is within MAX_LENGTH_USERNAME and not empty

    @param username is a string
    @return Boolean
    """
    notEmpty = username != ""
    withinLength = len(username) <= MAX_LENGTH_USERNAME
    return notEmpty and withinLength

def validPassword(password):
    """
    Checks if a username is within MAX_LENGTH_PASSWORD
    
    @param password is a string
    @return Boolean
    """
    withinLength = len(passsword) <= MAX_LENGTH_PASSWORD
    return withinLength

def validEMail(email):
    """
    Checks if an email is within MAX_LENGTH_EMAIL and of a valid format (using regex)
    
    @param email is a string
    @return Boolean
    """
    withinLength = len(email) <= MAX_LENGTH_EMAIL
    result = re.search('[A-Za-z0-9]*@[A-Za-z0-9]*\.[A-Za-z]{2,4}',email)
    if result:
        regexMatch = True
    else:
        regexMatch = False
    return withinLength and regexMatch

