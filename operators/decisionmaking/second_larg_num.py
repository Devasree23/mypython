num1=10
num2=20
num3=30

first=0
second=0
third=0

if((num1>num2) and (num1>num3)):
    first=num1
    if(num2>num3):
        second=num2
        third=num3
    else:
        second=num3
        third=num2
elif((num2>num1) and (num2>num3)):
    first=num2
    if(num1>num3):
        second=num1 
        third=num3 
    else:
        second=num3
        third=num1
elif((num3>num1) and (num3>num2)):
    first=num3 
    if(num1>num2):
        second=num1 
        third=num2
    else:
        second=num2
        third=num1 


print(first,second,third)
                           