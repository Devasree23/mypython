print("input is 123 and output will be 1+2+3=6")
num=123
sum=0
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
    sum+=digit
print("sum of the number:",sum)    