list=[5,2,4,15,35]
new_list=[]
for n in list:
    if n%5==0 and n%2!=0:
        new_list.append(n)
print(new_list)        
