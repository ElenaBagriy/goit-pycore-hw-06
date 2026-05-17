from collections import UserDict
from exceptions import (
    ValidationError,
    NotFoundError,
    ContactExistsError
)


class Field:
    """Base class for all fields."""

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Contact name field."""

    def __init__(self, value: str):
        self.validate_required(value)
        super().__init__(value)

    def validate_required(self, value: str):
        if not value.strip():
            raise ValidationError("The name is required")
        

class Phone(Field):
    """Phone number field."""

    def __init__(self, value: str):
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    def validate(self, value: str):
        """Validate phone number format (10 digits)."""
        if len(value) != 10 or not value.isdigit():
            raise ValidationError("The number must contain 10 digits")


class Record():
    """Stores contact name and list of phones."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value: str):
        if any(phone.value == value for phone in self.phones):
            return
        self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        phone = self.find_phone(value)
        if phone:
            self.phones.remove(phone)
            return
        raise NotFoundError("The phone is not found")

    def edit_phone(self, old_number: str, new_number: str):
        old_phone = self.find_phone(old_number)
        if not old_phone:
            raise NotFoundError("The phone is not found")
        new_phone = Phone(new_number)
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def find_phone(self, value: str):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Dictionary-based address book storage."""

    def add_record(self, record: Record):
        name = record.name.value
        if self.find(name):
            raise ContactExistsError("Contact already exists")
        self.data[name] = record

    def find(self, name: str):
        return self.data.get(name)
        
    def delete(self, name: str):
        if not self.find(name):
            raise NotFoundError("Contact not found")
        self.data.pop(name)



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")