class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return super().area()


c = Circle(5)  # important
print(c.area())

r = Rectangle(1, 4)
print(r.area())
