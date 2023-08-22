text="ABABC"
#first recursive character
new={}
for ch in text:
    if ch in new:
        print(ch,"is first recursive")
        break
    else:
        new[ch]=1    