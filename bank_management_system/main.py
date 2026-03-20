# Main file to run Bank Management System

from bank import Bank


def menu():
    print("\n===== Welcome to SmartBank System 🏦 =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")


def main():
    print("\nWelcome to SmartBank System 🏦")

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("❌ Invalid input! Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter name: ")

            try:
                age = int(input("Enter age: "))
                pin = int(input("Enter 4-digit PIN: "))
            except:
                print("❌ Invalid input for age or PIN")
                continue

            email = input("Enter email: ")

            user, msg = Bank.create_account(name, age, email, pin)
            print(msg)

            if user:
                print("💳 Account Number:", user['accountNo.'])

        elif choice == 2:
            acc = input("Enter account number: ")

            try:
                pin = int(input("Enter PIN: "))
                amt = int(input("Enter amount: "))
            except:
                print("❌ Invalid input")
                continue

            success, msg = Bank.deposit(acc, pin, amt)
            print(msg)

            if success:
                user = Bank.find_user(acc, pin)
                print("💰 Balance:", user['balance'])

        elif choice == 3:
            acc = input("Enter account number: ")

            try:
                pin = int(input("Enter PIN: "))
                amt = int(input("Enter amount: "))
            except:
                print("❌ Invalid input")
                continue

            success, msg = Bank.withdraw(acc, pin, amt)
            print(msg)

            if success:
                user = Bank.find_user(acc, pin)
                print("💰 Balance:", user['balance'])

        elif choice == 4:
            acc = input("Enter account number: ")

            try:
                pin = int(input("Enter PIN: "))
            except:
                print("❌ Invalid input")
                continue

            user = Bank.find_user(acc, pin)

            if user:
                print("\n📋 Account Details:")
                for k, v in user.items():
                    print(f"{k}: {v}")
            else:
                print("❌ User not found")

        elif choice == 5:
            acc = input("Enter account number: ")

            try:
                pin = int(input("Enter current PIN: "))
            except:
                print("❌ Invalid input")
                continue

            name = input("New name (Enter to skip): ")
            email = input("New email (Enter to skip): ")
            new_pin = input("New PIN (Enter to skip): ")

            success, msg = Bank.update_user(
                acc, pin,
                name or None,
                email or None,
                new_pin or None
            )

            print(msg)

        elif choice == 6:
            acc = input("Enter account number: ")

            try:
                pin = int(input("Enter PIN: "))
            except:
                print("❌ Invalid input")
                continue

            success, msg = Bank.delete_user(acc, pin)
            print(msg)

        elif choice == 7:
            print("🙏 Thank you for using SmartBank System")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
