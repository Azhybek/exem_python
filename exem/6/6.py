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

    def __area(self):
        print("Это приватный метод!")
        return self.width * self.height
    
    def __perimeter(self):
        print("Это приватный метод!")
        return 2 * (self.width + self.height)

    def __draw(self):
        print("Это приватный метод!")
        print(f"Drawing rectangle width width = {self.width} and height = {self.height}")

rect = Rectangle(10, 15)
rect.area()
print(rect.area())
print(rect.perimeter())
print(rect.draw())
# остаётся доступным под именем _ИмяКласса__ИмяАтрибута:
