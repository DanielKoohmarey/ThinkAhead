"""
Contains static variables that will be used throughout other files
"""

# The success return code
SUCCESS = 1

# Cannot find user/password pair in the database (for login only)
ERR_BAD_CREDENTIALS = -1

# Trying to add a user that already exists  (for add only)
ERR_USER_EXISTS = -2

# Trying to add an e-mail that already exists (for add only)
ERR_EMAIL_EXISTS = -3

# Invalid username (empty, or longer than MAX_USERNAME_LENGTH) (for add only)
ERR_BAD_USERNAME = -4

# Invalid password name (longer than MAX_PASSWORD_LENGTH) (for add only)
ERR_BAD_PASSWORD = -5

# Invalid E-mail (longer than MAX_EMAIL_LENGTH, or does not have an '@' character)
ERR_BAD_EMAIL = -6

# Query into a database using a username, or plannerID that is not registered
ERR_NO_RECORD_FOUND = -7

# Query into adding something (not username)to a database but it already exists 
ERR_RECORD_EXISTS = -8

# Error message on invalid semesters
ERR_INVALID_DATE = -9

MAX_USERNAME_LENGTH = 256
MAX_PASSWORD_LENGTH = 256
MAX_EMAIL_LENGTH = 256

SPRING_SEMESTER = 'Spring'
FALL_SEMESTER = 'Fall'
SUMMER_SEMESTER = 'Summer'

LOWER_DIVISION = 'Lower Division'
UPPER_DIVISION = 'Upper Division'

UNDERGRADUATE = 'Undergraduate'
GRADUATE = 'Graduate'
PROFESSIONAL = 'Professional'
