empty_list=[]
new_list=[]
length=int(input("enter the size of the list: "))
for i in range(length):
    num=int(input(f" enter {i}th position elements: "))
    empty_list.append(num)
maximum=max(empty_list)+10
empty_list.insert(2,maximum)
print(empty_list)    

    
    


    
        