class Planet:
    def __init__(self, orbit):
        self.orbit = orbit

class Mercury(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)

    def get_age(self, earth_age):
        res = earth_age * 365 // self.orbit
        return f'на Меркурии ваш возраст составляет {res} лет'

class Venus(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)

    def get_age(self, earth_age):
        res = earth_age * 365 / self.orbit * 365
        return f'на Венере ваш возраст составляет {round(res)} дней'

class Jupiter(Planet):
    def __init__(self, orbit):
        super().__init__(orbit)

    def get_age(self, earth_age):
        res = (earth_age * 365 // self.orbit) * (24 * 365)
        return f'на Юпитере ваш возраст составляет {res} часов'

merc = Mercury(88)
print(merc.get_age(20))

ven = Venus(225)
print(ven.get_age(20))

jup = Jupiter(12)
print(jup.get_age(20))