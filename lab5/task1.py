import re


class IncorrectNumber(Exception):
    def __init__(self, message="Incorrect phone number"):
        self.message = message
        super().__init__(self.message)


def check_phone_number(st):
    phone_pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    if re.match(phone_pattern, st):
        return True
    else:
        return False


def validate_number(st):
    if check_phone_number(st):
        return st
    else:
        raise IncorrectNumber()


st = input()
print(validate_number(st))