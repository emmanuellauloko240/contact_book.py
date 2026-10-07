# contact_book.py
 contact_book.py

# Contact Book

A command-line Python program for managing contacts — add, view, and delete contacts, with everything automatically saved to a file so your data persists between sessions.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
```bash
   git clone https://github.com/emmanuellauloko240/contact-book.git
```
3. Navigate into the project folder:
```bash
   cd contact-book
```
4. Run the program:
```bash
   python3 contact_book.py
```

## Features

- Add new contacts with a name and phone number
- View all saved contacts in a readable format
- Delete a contact by name
- Automatically saves contacts to a file (`contacts.json`)
- Loads previously saved contacts when the program starts

## What I Learned

Building this project helped me understand:

- Dictionaries, for storing structured data like name/phone pairs
- Lists of dictionaries, for managing multiple records
- Writing a menu-driven program using loops and `if`/`elif`/`else`
- Searching for and removing items from a list
- Saving and loading structured data using the `json` module
- Keeping sensitive data out of GitHub using `.gitignore`

There's still more to explore here — like organizing larger programs, and handling edge cases more gracefully — but this project gave me a much stronger grasp of how real, practical programs are structured.
        contacts.json
