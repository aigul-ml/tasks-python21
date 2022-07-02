class RadioMixin:
    def play_music(self, title):
        return f'Песня называется {title}'

class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(Auto, Boat):
    pass

auto = Auto()
boat = Boat()
obj = Amphibian()
print(auto.play_music('Call out my name'))
print(boat.play_music('Call out my name'))
print(obj.play_music('Call out my name'))