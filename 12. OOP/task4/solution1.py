class Taxi:
    def __init__(self, name, cost, cost_km):
       self.name = name
       self.cost = cost
       self.cost_km = cost_km

    def get_total_cost(self, km):
        trip_price = self.cost + self.cost_km * km
        return f'Такси {self.name}, стоимость поездки: {trip_price} сом'

taxi1 = Taxi('Namba', 45, 12)
taxi2 = Taxi('Jorgo', 46, 13)
taxi3 = Taxi('Yandex', 50, 14)

print(taxi1.get_total_cost(5))
print(taxi2.get_total_cost(6))
print(taxi3.get_total_cost(7))