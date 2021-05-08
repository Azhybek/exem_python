class Shape():

    def __init__(self):
        print("Shape created")

    def draw(self):
        print("Drawing a shape")

    def area(self):
        print("Calc area")

    def perimeter(self):
        print("Calc perimeter")

class Rectangle(Shape):
    
    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print("Rectangle created")

        Shape.area(self)

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f"Drawing rectangle width width = {self.width} and height = {self.height}")

rect = Rectangle(10, 15)
rect.area()
print(rect.area())
print(rect.perimeter())
print(rect.draw())