class ContactBook:
    def __init__(self):
        # Dictionary storing name as key and a dictionary of details as value
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Error: Contact '{name}' already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            print(f"Success: Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("Your contact book is empty.")
            return
        print("\n" + "=" * 30)
        print("          CONTACT LIST          ")
        print("=" * 30)
        for name, details in self.contacts.items():
            print(f"Name  : {name}")
            print(f"Phone : {details['phone']}")
            print(f"Email : {details['email']}")
            print("-" * 30)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"\nFound — Name: {name} | Phone: {contact['phone']} | Email: {contact['email']}")
        else:
            print(f"Error: Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Success: Contact '{name}' deleted.")
        else:
            print(f"Error: Contact '{name}' does not exist.")


# Main CLI Execution Loop
if __name__ == "__main__":
    book = ContactBook()
    
    # Pre-loading sample data
    book.add_contact("Alice Smith", "9876543210", "alice@email.com")
    book.add_contact("Bob Jones", "8765432109", "bob@email.com")

    while True:
        print("\n1. View All Contacts\n2. Add Contact\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            book.view_contacts()
        elif choice == "2":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            book.add_contact(name, phone, email)
        elif choice == "3":
            name = input("Enter name to search: ").strip()
            book.search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            book.delete_contact(name)
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")