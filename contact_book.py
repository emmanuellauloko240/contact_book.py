# contacts = [
#     {"name": "John", "phone": "123-456-7890"},
#     {"name": "Sarah", "phone": "987-654-3210"}
# ]

# print(contacts[0])
# print(contacts[0]["name"])
# print(contacts[1]["phone"])

def add_contact():
    name = input("What is your name: ")
    phone = input("What's your phone number: ")
    new_contact = {"name": name, "phone": phone}
    print(new_contact)

add_contact()
