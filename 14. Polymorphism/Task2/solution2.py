class Dog:
    def voice(self):
        print('Гав')

class Cat:
    def voice(self):
        print('Мяу')

barsik = Cat()
rex = Dog()

to_pet = lambda animal: animal.voice() # Можно, но не желательно

to_pet(barsik) 
to_pet(rex)