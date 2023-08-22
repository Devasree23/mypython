text="England promised to continue its aggressive approach to text test cricket"
for i in text.split():
    w=i.lower()
    if w.startswith("a"):
        print(w)
    elif w.startswith("e"):
        print(w) 
    elif w.startswith("i"):
        print(w)
    elif w.startswith("o"):
        print(w)
    elif w.startswith("u"):
        print(w)     
# ===========================================================
vowels=["a","e","i","o","u"]
words=text.split(" ")
for w in words:
    if w[0] in vowels:
        print(w)    
# ===============================================================
ws=[w for w in text.split(" ") if w[0].casefold() in vowels]      
print(ws)  
