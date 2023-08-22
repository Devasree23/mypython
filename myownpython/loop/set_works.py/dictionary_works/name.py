myprofile={"name":"devu",
           "age":21,
           "designation":"project assist"}
myprofile["salary"]=500000
print(myprofile)

for key in myprofile:
    print(f"{key}:{myprofile[key]}")

if("name" in myprofile):
    print(myprofile["name"])