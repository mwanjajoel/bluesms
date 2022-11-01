import requests

class SMS(self):
    # initialise the SMS class 
    def __init__(self, user, password, reciever, sender, message):
        self.user = user
        self.password = password
        self.reciever = reciever
        self.sender = sender
        self.message = message

    # method to send the SMS 
    def send(self, user, password, reciever, sender, message):

        api_url = "http://bluesmsuganda.com/api-sub.php?user={user}&password={password}&reciever={reciever}&sender={sender}&message={message}&,100"

        # make a get request to the API
        response = requests.get(api_url)

        return response

