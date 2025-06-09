class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder= account_holder
        self.initial_balance= initial_balance
    
    def deposit(self, amount):
        self.deposit