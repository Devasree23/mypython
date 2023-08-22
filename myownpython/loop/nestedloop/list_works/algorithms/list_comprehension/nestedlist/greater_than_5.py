lst=[[1,2,3],[2,3,4],[4,5,6]]
for sublst in lst:
    for num in sublst:
        if num>5:
            print(num)



greter_than_five=[num for sublst in lst for num in sublst if num>5]
print(greter_than_five)            