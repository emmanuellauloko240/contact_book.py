# contacts = [
#     {"name": "John", "phone": "123-456-7890"},
#     {"name": "Sarah", "phone": "987-654-3210"}
# ]

# print(contacts[0])
# print(contacts[0]["name"])
# print(contacts[1]["phone"])


# contacts = []

# def add_contact():
#     name = input("What is your name: ")
#     phone = input("What's your phone number: ")
#     new_contact = {"name": name, "phone": phone}
#     contacts.append(new_contact)
#     print(f"{name} added to contacts!")
# while True:
#     add_contact()
#     print(contacts)
#     again = input("Do you want to continue? (y/n): ")
#     if again != "y":
#         break


contacts = []


def add_contact():
    name = input("What is your name: ")
    phone = input("What's your phone number: ")
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    print(f"{name} added to contacts!")



while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Choose an option: ")
    # print(f"You chose: {choice}")
    if choice == "1":
        add_contact()
    elif choice == "2":
        print(contacts)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")