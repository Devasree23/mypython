from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def Draw(self):
        pass

class Triangle(Shape):
    def Draw(self):
        print("draw the triangle")

class Rectangle(Shape):
    def Draw(self):
        print("draw the Rectangle")


obj=Triangle()
obj.Draw() 
obj=Rectangle()
obj.Draw()           