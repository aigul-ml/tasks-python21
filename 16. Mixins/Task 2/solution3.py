class RadioMixin:
    def play_music(self, title):
        return 'Песня называется {0}'.format(title)

class Auto(RadioMixin):
    pass

class Boat(RadioMixin):
    pass

class Amphibian(Auto, Boat):
    pass

auto = Auto()
boat = Boat()
obj = Amphibian()
print(auto.play_music('We fell in love in october'))
print(boat.play_music('We fell in love in october'))
print(obj.play_music('We fell in love in october'))