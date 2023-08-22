age=int(input("enter the age:"))

if age<18:
    raise Exception("invalid error")
else:
    print("valid")