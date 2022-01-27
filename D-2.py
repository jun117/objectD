class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)

    def diagonal(self):
        return ((self.height ** 2 + self.width ** 2) ** 0.5)


rectangle1 = Rectangle(height=5, width=6)

print(rectangle1.area())
print(rectangle1.diagonal())
