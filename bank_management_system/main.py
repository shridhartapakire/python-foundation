# Main file to run Bank Management System

from bank import Bank

def menu():
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")


def main():
    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            pin = int(input("Enter 4-digit PIN: "))

            user, msg = Bank.create_account(name, age, email, pin)
            print(msg)
            if user:
                print("Account Number:", user['accountNo.'])

        elif choice == 2:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
            amt = int(input("Enter amount: "))

            success, msg = Bank.deposit(acc, pin, amt)
            print(msg)

        elif choice == 3:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))
            amt = int(input("Enter amount: "))

            success, msg = Bank.withdraw(acc, pin, amt)
            print(msg)

        elif choice == 4:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))

            user = Bank.find_user(acc, pin)
            if user:
                print("\nUser Details:")
                for k, v in user.items():
                    print(f"{k}: {v}")
            else:
                print("User not found")

        elif choice == 5:
            acc = input("Enter account number: ")
            pin = int(input("Enter current PIN: "))

            name = input("New name (or press Enter): ")
            email = input("New email (or press Enter): ")
            new_pin = input("New PIN (or press Enter): ")

            success, msg = Bank.update_user(acc, pin, name or None, email or None, new_pin or None)
            print(msg)

        elif choice == 6:
            acc = input("Enter account number: ")
            pin = int(input("Enter PIN: "))

            success, msg = Bank.delete_user(acc, pin)
            print(msg)

        elif choice == 7:
            print("Thank you!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
