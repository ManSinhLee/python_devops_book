class BankAccount:
    def __init__(self, ACCOUNT_HOLDER, BALANCE):
        self._account_holder = ACCOUNT_HOLDER  # protected attribute
        self._balance = BALANCE  # protected attribute

    def get_account_holder(self):
        return self._account_holder

    def get_balance(self):
        return self._balance

    def deposit(self, AMOUNT):
        if AMOUNT > 0:
            self._balance += AMOUNT
            print(f"Deposited ${AMOUNT}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, AMOUNT):
        if 0 < AMOUNT <= self._balance:
            self._balance -= AMOUNT
            print(f"Withdrew ${AMOUNT}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Creating an instance of the BankAccount class
account = BankAccount(ACCOUNT_HOLDER="Man Sinh Lee", BALANCE=1000)

# Accessing attributes using public methods
print(f"Account Holder: {account.get_account_holder()}")
print(f"Current Balance: ${account.get_balance()}")

# Depositing and withdrawing
account.deposit(500)
account.withdraw(200)
