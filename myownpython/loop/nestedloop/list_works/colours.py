colours=["red","green","purple","orange","rose"]
print(len(colours))

for i in range(0,len(colours)):
    print(colours[i])

colours[1]="cyan"
print(colours) 

for i in range(0,2):
    colours[i]=["red","apple","black"]
    print(colours)


print()

for c in colours:
    print(c)