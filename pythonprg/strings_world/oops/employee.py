class employee:
    id:int
    name:str
    desig:str
    salary:int
    def set_emp(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    def get_emp(self):
        print(self.id,self.name,self.desig,self.salary)

emp1=employee()
emp1.set_emp(1000,"devu","CEO",1000000)   
emp1.get_emp()         
