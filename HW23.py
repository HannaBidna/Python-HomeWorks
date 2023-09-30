import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        self.x +=other.x
        self.y += other.y
        return self

    def __str__(self):
        return f'Point ({self.x}, {self.y})'


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        if radius == 0:
            return Point(x, y)
        else:
            return Circle(radius, x, y)

    def __str__(self):
        if self.radius == 0:
            return f'Point ({self.x}, {self.y}), radius = 0'
        else:
            return f'Circle ({self.radius}, {self.x}, {self.y})'

a = Circle(5, 2, -10)
b = Circle(5, 6, -4)
c = a - b
print(c)

a_1 = Circle(10, 4, -8)
b_1 =Circle(3, 4, -9)
c_1 = a_1 - b_1
print(c_1)


a_2 = Circle(3, 4, -8)
b_2 =Circle(8, 0, 9)
c_2 = a_2 - b_2
print(c_2)
