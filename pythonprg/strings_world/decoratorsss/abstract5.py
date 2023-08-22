from datetime import date
class Operators:
    num1:int
    num2:int
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def product(self):
        return self.num1*self.num2
    @staticmethod
    def get_date():
        return date.today()
    
obj=Operators(100,200)
print(obj.add())
print(obj.product()) 
print(Operators.get_date())   
        
