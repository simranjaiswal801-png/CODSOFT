import math

history = []

while True:
    print("\n--- Advanced Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Show History")
    print("9. Clear History")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Calculator closed.")
        break

    if choice == "6":
        num = float(input("Enter number: "))
        result = math.sqrt(num)
        print("Result:", result)
        history.append(f"√{num} = {result}")
        continue

    if choice == "8":
        print("\nHistory:")
        for h in history:
            print(h)
        continue

    if choice == "9":
        history.clear()
        print("History cleared.")
        continue

    if choice not in ["1","2","3","4","5","7"]:
        print("Invalid choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        op = "+"

    elif choice == "2":
        result = num1 - num2
        op = "-"

    elif choice == "3":
        result = num1 * num2
        op = "*"

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
            continue
        result = num1 / num2
        op = "/"

    elif choice == "5":
        result = num1 ** num2
        op = "^"

    elif choice == "7":
        result = num1 % num2
        op = "%"

    print("Result:", result)
    history.append(f"{num1} {op} {num2} = {result}")