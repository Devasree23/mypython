data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }
wc={}
for k,v in data.items():
    if v in wc:
        wc[v].append(k)
    else:
        wc[v]=[k]   
print(wc)        