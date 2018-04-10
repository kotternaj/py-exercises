class Account:
    def __init__(self, owner, balance): 
        self.owner = owner
        self.balance = balance       

    def deposit(self, depValue):
        if depValue >= 100: 
            print('You cannot deposit that much at once')
            mainloop()
        else: 
            self.balance += depValue
            return f'Your balance is now: ${self.balance}'

    def withdraw(self, withValue):
        if self.balance < withValue:
            print('You dont have enough funds in your account to withdraw that much')
            mainloop()            
        else:
            self.balance -= withValue
            return f'Your balance is now: ${self.balance}'
    
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    
def mainloop():

    acct = Account('Bob', 100)
    funds = int(input('Enter an amount to add to your account: '))
    print(acct.deposit(funds))
    funds = int(input('Enter an amount to withdraw from your account: '))
    print(acct.withdraw(funds))

mainloop()