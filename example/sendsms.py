from bluesms.sms import SMS 

# initialise the SMS class
sms = SMS()

# send the SMS 
try: 
    sending = sms.send(user="user@example.com", password="password", reciever="0777xxxxxx", sender="sender", message="message")

    print("The SMS sent", sending.text)

except Exception as e:
    print("Error sending SMS:", e)