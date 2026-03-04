import random
import string

while True:
    print("\n=== Advanced Password Generator ===")
    print("1. Letters only")
    print("2. Numbers only")
    print("3. Strong password")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "4":
        print("Program closed.")
        break

    length = int(input("Enter password length: "))

    if choice == "1":
        chars = string.ascii_letters

    elif choice == "2":
        chars = string.digits

    elif choice == "3":
        chars = string.ascii_letters + string.digits + string.punctuation

    else:
        print("Invalid choice!")
        continue

    password = "".join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)