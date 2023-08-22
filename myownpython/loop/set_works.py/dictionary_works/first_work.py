emp={"name":"hari",
     "id":102,
     "desig":"HR",
     "salary":500000}
print(emp)

print(emp["name"])
print(emp["salary"])

for key in emp:
    print(key,emp[key])
emp["gender"]="male"
print(emp)    
emp["salary"]=270000000
print(emp)
print(emp["salary"])
emp["salary"]+=2000
print(emp["salary"])

print("gender" in emp)
if("name" in emp):
    print("present")
else:
    print("not present")    

