class Books:
    id:int
    name:str
    price:int
    author:str
    def __init__(self,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.author=kwargs.get("author")
    def __str__(self):
        return self.name
    def get_student(self):
        print(self.id,self.name,self.price,self.author)




obj=Books(id=101,name="randamoozham",price=560,author="mt")  
print(obj)
obj.get_student() 
