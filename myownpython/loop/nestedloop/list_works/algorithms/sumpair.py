lst=[2,3,4,5]
sum=7

for i in lst:
    for j in lst:
        if (i!=j and i<j):
            current_sum=i+j
            if(current_sum==sum):
                print(i,j)   