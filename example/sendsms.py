from src.sms import SMS

# initialise the SMS class
sms = SMS()

# send the SMS 
sending = sms.send(user="username", password="password", reciever="256772123456", sender="256772123456", message="Hello World")

print("SMS sending", sending)