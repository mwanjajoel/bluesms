import re

# Validate phone numbers 
def validate_phone_number(phone_number):
    try:
        return re.match('^\+\d{1,3}\d{3,}$', phone_number)
    except ValueError:
        return False