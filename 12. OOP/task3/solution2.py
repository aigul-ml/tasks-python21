class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= amount
        print('Ваш баланс: ' + str(self.balance) + ' сом')

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print('Ваш баланс: ' + str(self.balance) + ' сом')

account = BankAccount()

account.deposit(1000) 
account.withdraw(500)