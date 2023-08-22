print("find the BMI of a person")
print("enter the weight")
weight=80
print("enter the height")
height_cm=165
height_m=height_cm/100
bmi=weight/(height_m)**2
print(f"bmi is {bmi}")
#checking the weight categories
if(bmi<18.5):
    print("underweight")
elif(18.5 <= bmi < 24.9): 
    print(" normal weight")  
elif(25.0 <= bmi < 29.9):
    print("overweight")    
elif(30.0 <= bmi < 34.9):
    print("obesity class1")    
elif(35.0 <= bmi < 39.9):
    print("obesity class2")    
elif(bmi>40):    
    print("obesity class3")



