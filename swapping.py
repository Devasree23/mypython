num1=10
num2=20
print(f"values b4 swapping a={num1} and b={num2}")

# another way 1
# temp=a
# a=b
# b=temp
# print(f"values after swapping a={a} and b={b}")

#logic2
# (num1,num2)=(num2,num1)
# print(f"values after swapping num1={num1} and num2={num2}")


#logic 3
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"num1={num1}, num2={num2}")