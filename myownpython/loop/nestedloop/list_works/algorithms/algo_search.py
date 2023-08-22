lst=[2,3,4,5,6,8,9]
elem=80
low=0
is_found=False
upp=len(lst)-1
while(upp>=low):
    mid=(upp+low)//2
    if elem==lst[mid]:
        is_found=True
        break
    elif elem>lst[mid]:
        low=mid+1
    elif elem<lst[mid]:
        upp=mid-1  
print("element found" if is_found==True else "element not found")          