data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }
wc={}
for v in data.values():
    if v in wc:
        wc[v]+=1
    else:
        wc[v]=1 
print(wc)           

