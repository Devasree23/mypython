num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

try:
    res=num1/num2
    print("result:",res)
except Exception as e:
    print("error occured")  

print("db commit1")
print("db commit2")      