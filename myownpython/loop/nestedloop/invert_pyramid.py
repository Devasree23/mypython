for row in range(6,1,-1):
    for col in range(row-1):
        print("*",end=" ")
    print() 


for row in range(1,6):
    for col in range(6,row,-1):
        print("*",end=" ")
    print()    