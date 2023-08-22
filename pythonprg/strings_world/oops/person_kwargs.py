class Student:
    rollno:int
    name:str
    course:str

    def __init__(self,**kwargs):
        self.rollno=kwargs.get("rollno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")


        print(kwargs)

    def get_student(self):
        print(self.rollno,self.name,self.course)

    def __str__(self):
        return self.name  


obj=Student(rollno=101,name="devu",course="bca") 
obj.get_student() 
print(obj)
      