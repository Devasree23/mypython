words=["hello","hai","in","Aabbccddeeff","aabbccddeeff","good","perfect"]
print(max(words,key=lambda w:len(w)))
print(min(words,key=lambda w:len(w)))