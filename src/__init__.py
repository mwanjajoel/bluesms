# initialise the SMS app

def initialise(username, password):
     if username is None or password is None:
         raise ValueError('username and or password must be set')