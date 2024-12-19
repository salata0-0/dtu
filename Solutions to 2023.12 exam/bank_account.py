class  BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return amount
        
        return 0
            
        
    def get_balance(self):
        return self.balance
    
class OverdraftAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return amount
        
        return 0
