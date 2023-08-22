number=[2,7,8,9,12,13]
odds=[]
evens=[]

for num in number:
    if num%2==0:
        even=num
        evens.append(even)
    else:
        odd=num
        odds.append(odd)    
print(evens)
print(odds)        