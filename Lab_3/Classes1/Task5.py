class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} balance is {self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

Bank_Account = Account("Dimash", 100000)
Bank_Account.deposit(100)
Bank_Account.withdraw(200)
print(Bank_Account)