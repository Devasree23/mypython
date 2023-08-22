text="one 100 and fifty 5"
for i in text.split(" "):
    if i.isdigit():
        print(i)


num=[w for w in text.split(" ") if w.isdigit()]    
print(num)    