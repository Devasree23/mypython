class Student:
    rolno:int
    name:str
    course:str
    
    def __init__(self,rol,name,course):
        self.rolno=rol
        self.name=name
        self.course=course
    def get_student(self):
        print(self.rolno,self.name,self.course)        
obj=Student(1000,"hari","java")
obj.get_student()

obj2=Student(1001,"jeeva","python")
obj2.get_student()