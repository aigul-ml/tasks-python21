class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

barsik = Cat()
rex = Dog()

def to_pet(animal):
    animal.voice()

to_pet(barsik)
to_pet(rex)