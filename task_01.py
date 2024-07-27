from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Class to save names
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)
    @staticmethod
    def validate(phone):
        # Validate phone number format: must be 10 digits
        return phone.isdigit() and len(phone) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Add a phone number to the record
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Remove a phone number from the record
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Edit an existing phone number in the record
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        # Find a phone number in the record
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        # Return a string of the record
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Add a record to the address book
        self.data[record.name.value] = record

    def find(self, name):
        # Find a record by name in the address book
        return self.data.get(name, None)

    def delete(self, name):
        # Delete a record by name from the address book
        if name in self.data:
            del self.data[name]

# Create new address book
book = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John to the address book
book.add_record(john_record)

 # Create and add new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Display all record in the book 
for name, record in book.data.items():
    print(record)

# Search and edit the phonr for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Display: Contact name: John, phones: 1112223333; 5555555555

# Find a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Display: 5555555555

 # Delete Jane
book.delete("Jane")
