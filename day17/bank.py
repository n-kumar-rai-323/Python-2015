class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder= account_holder
        self.balance= initial_balance
        print(f"Account created for {self.account_holder} with initial balance: Rs.{self.balance:.2f}")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount: .2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if(amount <= 0):
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds. Attempted to withdraw Rs.{amount:.2f}")
        else:
            self.balance -=amount
            print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")
    def get_balance(self):
        print(f"Current balance for {self.account_holder}: Rs.{self.balance:.2f}")

print("------ Creating Account -------")
my_account =BankAccount("Nishan Kumar Rai", 1000.00)
my_account.deposit(2000.00)
my_account.withdraw(2000.00)
my_account.get_balance()