from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass


class Swift(Car):
    def start(self):
        print("start the car")
            

obj=Swift()
obj.start()            