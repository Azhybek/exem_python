from abc import abc
from abc import abstractmethod

class Shape():

    def __init__(self):
        print("Shape created")

    def draw(self):
        print("Drawing a shape")

    def area(self):
        print("Calc area")

    def perimeter(self):
        print("Calc perimeter")

class Shape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def draw (self):
        pass

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass 
        
    def drag(self):
        print("Необезян переопределять")

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

    def drag(self):
        super()._drag()
        print("Actional actions")
    