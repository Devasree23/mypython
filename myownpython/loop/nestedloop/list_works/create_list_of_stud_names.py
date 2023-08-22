stud_name=[]
length=int(input("enter the size of list: "))

for i in range(length):
    name=input("enter the names:")
    stud_name.append(name)
check_name=input("enter a name:")

for s in range(length): 
    if(stud_name[s]==check_name):
        stud_name[s]="anamika"
        break
    elif(s==length-1):
        stud_name.insert(1,"Amal")
print(stud_name)        
