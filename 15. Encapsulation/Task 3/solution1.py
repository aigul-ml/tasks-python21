class Car:
    __speed = 0

    def set_speed(self, speed):
        self.__speed = speed

    def show_speed(self):
        return self.__speed

car1 = Car()

print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed())