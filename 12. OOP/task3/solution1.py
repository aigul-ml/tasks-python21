class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.amount = amount
        BankAccount.balance -= amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

    def deposit(self, amount):
        self.amount = amount
        BankAccount.balance += amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

account = BankAccount()

account.deposit(1000) 
account.withdraw(500) 