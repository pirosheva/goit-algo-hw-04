def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    for contact in contacts:
        if contact == name:
            contacts[contact] = phone
            return "Contact changed"
    return "Contact not finded"

def print_phone_username(args, contacts):
    name = args[0]
    return contacts.get(name)

def show_all(contacts):
    for contact in contacts:
        print(contact + " " + contacts[contact])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(print_phone_username(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
