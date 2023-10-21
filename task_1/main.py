from input_error import input_error


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "Contact exists, please use command 'change' for changing contact."

    contacts[name] = phone

    return "Contact added."


@input_error
def get_contact(args, contacts):
    name = args[0]

    return f"{name}: {contacts[name]}"


def get_all_contacts(contacts):
    all_contacts = ""

    for name, phone in contacts.items():
        all_contacts += f"{name}: {phone}\n"

    if all_contacts == "":
        return "Contact list is empty."

    return all_contacts


@input_error
def change_contact(args, contacts):
    name, phone = args

    if contacts[name]:
        contacts[name] = phone

    return "Contact changed."


def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
