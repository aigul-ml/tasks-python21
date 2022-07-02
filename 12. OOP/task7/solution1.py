from datetime import date

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner
    
    def get_year(self):
        current_year = date.today().year
        return f'выиграл {current_year - self.year} лет назад' 

winner1 = Nobel('Литература', 1971, 'Пабло Неруда') 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())
  
winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ') 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())