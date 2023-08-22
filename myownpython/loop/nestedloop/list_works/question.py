arr=[2,3,4]
output=[]
total_sum=sum(arr)
print(total_sum)


for sub in arr:
    subtract=total_sum-sub
    output.append(subtract)
print(output)    
