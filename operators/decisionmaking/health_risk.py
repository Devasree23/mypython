tummy_size=56
buttock_sze=46

value=tummy_size/buttock_sze

gender=1
male=0
female=1

if(gender==male):
    print("health rate of male")
    if(value<0.95):
        print("health rate low")
    elif(value<=1.0):
        print("health rate moderate")
    elif(value>1.0):
        print("health rate high ")
else:
    print("heart rate of female")
    if(value<0.80):
        print("health rate low")
    elif(value<=0.85):
        print("health rate moderate")
    elif(value>0.85):
        print("health rate high ")       