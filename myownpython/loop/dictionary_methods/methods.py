student={"name":"devu","age":21,"rollno":1234}
print(student.values())
print(student.keys())
print(student.items())

for k,v in student.items():
    print(k,v)

print(student.get("name"))
student.pop("rollno")
print(student)