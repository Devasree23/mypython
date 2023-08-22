class bank:
    accno:int
    p_name:str
    balance:int
    ac_type:str
    amount:int
    def create_account(self,accno,balance,ac_type):
        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
    def deposit(self,amount):
            self.balance+=amount
            print(f"your balance is:{self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your sbk acc {self.accno} has been debited with amount {amount} aval bal is {self.balance}")
        else:
             print("transaction failed")   

obj1=bank() 
obj1.create_account(100,2000,"savings")    
obj1.withdraw(1000)    
      

