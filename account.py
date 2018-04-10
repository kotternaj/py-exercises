class Account:
    def __init__(self, owner, balance): 
        self.owner = owner
        self.balance = balance       

    def deposit(self, depValue):
        self.balance += depValue
        return f'Your balance is now: ${self.balance}'
    def withdraw(self):
        pass
    
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    # def add_to_value(self)

acct = Account('Bob', 100)
funds = int(input('Enter an amount to add to your account: '))
print(acct.deposit(funds))


