import math

class Circle:
    color = 'Синий'
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * self.radius ** 2

circle = Circle(2)
circle.color = 'Красный'

print(circle.color)
print(circle.get_area())