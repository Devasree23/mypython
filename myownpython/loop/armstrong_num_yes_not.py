num=163
original=num
count=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    print(digit)
    sum=sum+digit**count
    num=num//10
if(sum==original):
    print("the num is armstrong number",sum)    
else:
    print("the number is not armstrong number",sum)    