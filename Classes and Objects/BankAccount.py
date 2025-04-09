# Design a BankAccount class with methods for deposit, withdrawal, and checking balance. Include appropriate error handling.

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def deposit(self):
        try:
            amount = int(input('Enter deposit amount: '))
            if amount < 0:
               print("Error: negative values not allowed")
            else:
                self.balance += amount
                print(f"Deposit successful. New balance: {self.balance}")

        except Exception:
            print("Error: enter a number only!")

    def withdrawal(self):
        try:
            amount = int(input('Enter withdrawal amount: '))
            if amount < 0:
               print("Error: negative values not allowed")
            
            if self.balance < amount:
                print("Error: insufficient funds")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: {self.balance}")

        except Exception:
            print("Error: enter a number only!")

    def checkBalance(self):
        try:
            print(f"Bank balance: {self.balance}")
        except Exception as ex:
            print(ex)
        pass


account1 = BankAccount()

account1.checkBalance()
account1.withdrawal()

account1.deposit()
account1.checkBalance()

account1.withdrawal()
account1.checkBalance()