class Circle:
    color = 'Синий'
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.pi * pow(self.radius, 2)

circle = Circle(2)
circle.color = 'Красный'

print(circle.color)
print(circle.get_area())