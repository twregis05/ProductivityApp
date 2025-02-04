class UserAlreadyExistsError(Exception):
    # Raised when attempting to create a user that already exists
    pass

class InvalidNameError(Exception):
    # Raised when attempting to create a user with an invalid name
    pass

class InvalidUsernameError(Exception):
    # Raised when creating/entering a username that is not valid
    pass

class InvalidEmailError(Exception):
    # Raised when user enters an invalid email
    pass

class InvalidPasswordError(Exception):
    # Raised when creating/entering password that does not meet security requirements
    pass

class NonMatchingPasswordError(Exception):
    # Raised when user is creating an account and
    # the password confirmation does not match the password initially entered
    pass

class AuthenticationError(Exception):
    # Raised when login credentials are incorrect
    pass

