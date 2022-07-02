class Money:
    def __init__(self, country, symbol):
        self.country = country
        self.symbol = symbol
    
class Dollar(Money):
    rate = 84.80

    def exchange(self, amount):
        res = self.rate * amount
        return f'$ {amount} равен {res} сомам'

class Euro(Money):
    rate = 98.40

    def exchange(self, amount):
        res = self.rate * amount
        return f'€ {amount} равен {res} сомам'