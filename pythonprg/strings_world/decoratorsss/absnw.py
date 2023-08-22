lst=["hunter","gixer"]
class Parent:
    def vehicle(self):
        self.context=["passionpro","swift"]
        return self.context
    
class Child(Parent): 
    def vehicle(self):
        self.context=super().vehicle()
        self.context.append("hunter")
        return self.context
class Child2(Parent):
    def vehicle(self):
        self.context=super().vehicle()
        self.context.extend(lst)
        return self.context
class Child3(Child2):
    def vehicle(self):
        self.context=super().vehicle()
        self.context.remove("hunter")
        self.context.append("kl15")

        return  self.context       


obj=Child()
print(obj.vehicle())  
obj=Child2()
print(obj.vehicle()) 
obj=Child3()
print(obj.vehicle())  