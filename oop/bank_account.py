# bank_account.py
# Python OOP Practice – Bank Account Example


class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

    def display_balance(self):
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: {self.balance}")


# Creating account object
account1 = BankAccount("Alice", 1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.display_balance()
