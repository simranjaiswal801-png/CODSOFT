contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} | {info['phone']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("❌ Contact not found")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        contacts[name]["phone"] = input("New phone: ")
        contacts[name]["email"] = input("New email: ")
        contacts[name]["address"] = input("New address: ")
        print("✅ Updated successfully")
    else:
        print("❌ Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("🗑 Deleted successfully")
    else:
        print("❌ Contact not found")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice")