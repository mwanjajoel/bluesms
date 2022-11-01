from sms import SMS

# initialise the SMS class
sms = SMS()

# send the SMS 
try: 
    sending = sms.send(user="kisfredgmailcom", password="P@haneroo@120", reciever="0777222823", sender="API User", message="Hello from BlueSMS SDK")
    print("The SMS sent", sending.text)
except Exception as e:
    print("Error sending SMS:", e)
