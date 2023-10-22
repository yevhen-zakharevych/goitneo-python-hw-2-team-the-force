from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, name, phones):
        if len(phones) == 0:
            raise ValueError

        record = Record(name)

        for phone in phones:
            record.add_phone(phone)

        self.data[record.name.value] = record

        return "Contact has been added."

    def edit_record(self, name, old_phone, new_phone):
        record = self.find(name)
        record.edit_phone(old_phone, new_phone)

    def find(self, name):
        return self.data[name]

    def find_phone(self, name, phone):
        record = self.find(name)

        return record.find_phone(phone)

    def delete(self, name):
        del self.data[name]

