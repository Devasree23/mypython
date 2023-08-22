text="ABBAACD"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1    
print(wc)  
#count is available now and find the most recursive of the number
print(max(wc,key=lambda k:wc.get(k)))
print(min(wc,key=lambda k:wc.get(k)))