import requests

class SMS(): 
    
    # method to send the SMS 
    def send(self, user, password, reciever, sender, message):
        self.user = user
        self.password = password
        self.reciever = reciever
        self.sender = sender
        self.message = message

        api_url = "http://bluesmsuganda.com/api-sub.php?user={}&password={}&reciever={}&sender={}&message={}&,100".format(user, password, reciever, sender, message)

        # check if the user is not empty
        if self.user == "":
            raise Exception("Please provide the username")

        # make a get request to the API
        response = requests.get(api_url)
        return response

