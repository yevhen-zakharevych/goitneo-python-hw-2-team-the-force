from phone_length_exception import PhoneLengthException
from phone_exception import PhoneException


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact does not exist."
        except PhoneLengthException:
            return "Phone length should be 10."
        except PhoneException:
            return "Phone does not exist."

    return inner
