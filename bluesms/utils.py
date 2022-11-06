import re


def validate_phone_number(phone_number) -> bool:
    """
    Expects number to start with country code.
    For example +256703000000
    """
    try:
        return bool(re.match('^\+\d{1,3}\d{3,}$', phone_number))
    except ValueError:
        return False
