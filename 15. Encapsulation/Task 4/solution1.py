class Car:
    __speed = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

car1 = Car()

print(car1.speed) 
car1.speed = 20 
print(car1.speed) 