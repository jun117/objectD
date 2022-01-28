class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return (self.side * self.side)

    def diagonal(self):
        return ((self.side ** 2 + self.side ** 2) ** 0.5)


square1 = Square(side=1.5)
square2 = Square(side=15)

print(square1.area())
print(square1.diagonal())

print(square2.area())
print(square2.diagonal())
