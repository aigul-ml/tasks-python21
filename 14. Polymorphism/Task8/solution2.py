class Planet:
    def __init__(self, name):
        self.name = name

class Mercury(Planet):
    def __init__(self, orbit):
        self.orbit = orbit

    def get_age(self, earth_age):
        res = earth_age * 365 // self.orbit
        return 'на Меркурии ваш возраст составляет ' + str(res) + ' лет'

class Venus(Planet):
    def __init__(self, orbit):
        self.orbit = orbit

    def get_age(self, earth_age):
        res = round((earth_age * 365) * (365 / self.orbit))
        return 'на Венере ваш возраст составляет ' + str(res) +' дней'

class Jupiter(Planet):
    def __init__(self, orbit):
        self.orbit = orbit

    def get_age(self, earth_age):
        res = (earth_age * 365 // self.orbit) * (365 * 24)
        return 'на Юпитере ваш возраст составляет ' + str(round(res)) + ' часов'

ven = Venus(12)
print(ven.get_age(20))

jup = Jupiter(88)
print(jup.get_age(20))

merc = Mercury(225)
print(merc.get_age(20))