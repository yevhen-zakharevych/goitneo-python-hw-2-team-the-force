from field import Field
from phone_length_exception import PhoneLengthException


class Phone(Field):
    def __init__(self, value):
        if len(value) < 10:
            raise PhoneLengthException
        super().__init__(value)
