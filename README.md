# goit-pycore-hw-06 - Address Book CLI (OOP Project)

This project is a simple object-oriented implementation of an address book in Python. It was developed as part of a learning assignment to practice classes, inheritance, and data encapsulation.

## Features

The application allows you to:

- Add contacts to the address book
- Store multiple phone numbers per contact
- Find contacts by name
- Edit existing phone numbers
- Remove phone numbers
- Delete contacts from the address book

## Project Structure

### Core Classes

- **Field** – base class for all fields
- **Name** – required field for contact name
- **Phone** – phone number field with validation (must contain exactly 10 digits)
- **Record** – represents a contact with a name and multiple phone numbers
- **AddressBook** – stores and manages all contact records (based on `UserDict`)

## Example Usage

```python
# Create address book
book = AddressBook()

# Create a record
john = Record("John")
john.add_phone("1234567890")
john.add_phone("5555555555")

# Add record to book
book.add_record(john)

# Find and update contact
contact = book.find("John")
contact.edit_phone("1234567890", "1112223333")

# Print contact
print(contact)

# Delete contact
book.delete("John")
````

## Validation Rules

* Name is required and cannot be empty
* Phone number must contain exactly 10 digits

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* `collections.UserDict`

## Purpose

This project demonstrates OOP principles such as:

* Encapsulation
* Inheritance
* Composition
* Data validation
* Basic in-memory data management
