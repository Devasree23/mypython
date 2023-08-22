from json import load

with open("C:\\Users\\vaisa\\OneDrive\\Desktop\\pythonprg\\strings_world\\fileinputoutput\\jsonworks\\data.json","r")as f:
    data=load(f)

for u in data:
    print(u.get("name"))
#student with highest mark
candidate=max(data,key=lambda s:s.get("total"))
print(candidate)

candidate=sorted(data,reverse=True, key=lambda s:s.get("total"))
print(candidate)

candidate=min(data,key=lambda s:s.get("total"))
print(candidate)

bca_students=[u.get("name") for u in data if u.get("course")=="bca"]
print(bca_students)
