employee={"id":12,"name":"adhi","designation":"hr","salary":200000}

def get_name(st):
    return st.get("name")
print(get_name(employee))

#lambda fun
get_name=lambda st:st.get("name")
print(get_name(employee))


get_salary=lambda emp:emp.get("salary")
print(get_salary(employee))