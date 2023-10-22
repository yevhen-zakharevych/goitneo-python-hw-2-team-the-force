from input_error import input_error
from address_book import AddressBook


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, book):
    name, *phones = args

    return book.add_record(name, phones)


@input_error
def get_contact(args, book):
    name = args[0]

    return str(book.find(name))


@input_error
def find_phone(args, book):
    name, phone = args

    return book.find_phone(name, phone)


def get_all_contacts(book):
    res = ""

    for name, record in book.data.items():
        res += f"{str(record)}\n"

    if res == "":
        return "Address book is empty."

    return res


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args

    book.edit_record(name, old_phone, new_phone)

    return "Contact changed."


@input_error
def delete_contact(args, book):
    name, = args

    book.delete(name)

    return "Contact has been deleted."


def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_contact(args, book))
        elif command == "find":
            print(find_phone(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "delete":
            print(delete_contact(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
