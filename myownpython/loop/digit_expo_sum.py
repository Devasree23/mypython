num=370
sum=0
while(num!=0):
    digit=num%10#123%10=3
    print(f"{digit}** ={digit**3}")
    cube=digit**3
    sum=sum+cube
    num=num//10
print(sum)    
    