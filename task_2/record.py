from name import Name
from phone import Phone
from phone_exception import PhoneException


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def find_phone(self, phone):
        phones = list(map(lambda p: p.value, self.phones))

        if phone in phones:
            return f"{self.name.value}: {phone}"
        else:
            raise PhoneException

    def edit_phone(self, old_phone, new_phone):
        phones = list(map(lambda p: p.value, self.phones))

        if old_phone in phones:
            index = phones.index(old_phone)
            self.phones[index] = Phone(new_phone)

        else:
            raise PhoneException

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
