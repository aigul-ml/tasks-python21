class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2 

class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def get_area(self):
        return (self.height * self.base) // 2

class Pyramid(Triangle, Square):
    def get_volume(self):
        a = int(1 / 3 * (self.base**2) * self.height)
        return a

s = Square(5)
t = Triangle(3,2)
p = Pyramid(3,2)

print(s.get_area())
print(t.get_area())
print(p.get_volume())