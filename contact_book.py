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

import json

def save_contacts():
    with open("contacts.json","w") as file:
        json.dump(contacts, file)

def load_contacts():
    try:
        with open("contacts.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

contacts = load_contacts()

def add_contact():
    name = input("What is your name: ")
    phone = input("What's your phone number: ")
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    print(f"{name} added to contacts!")


def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def delete_contact():
    name = input("Which contact do you want to delete? ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"{name} deleted.")
            return
    print(f"No contact named {name} found.")
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Choose an option: ")
    # print(f"You chose: {choice}")
    if choice == "1":
        add_contact()
        save_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
        save_contacts()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")