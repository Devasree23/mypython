num1 = 10
num2 = 20
num3 = 30
if num1 < num2:
    if num2 < num3:
        print (num1, "<", num2, "<", num3)
    else:
        if num1 < num3:
            print (num1, "<", num3, "<", num2)
        else:
            print (num3, "<", num1, "<", num2)
else:
    if num3 < num2:
        print (num3, "<", num2, "<", num1)
    else:
        if num3 < num1:
            print (num2, "<", num3, "<", num1)
        else:
            print (num2, "<", num1, "<", num3)