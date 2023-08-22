lst=[1,3,4,5,8,9]
elem=2
flag=0
for i in range(0,len(lst)):
    if elem==lst[i]:
        flag=1
        break
if flag==1:
    print("element found") 
else:
    print("element not found")            
       