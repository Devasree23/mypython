def addition(*args):
    return sum(args)
print(addition(10,20))
print(addition(10,20,30,40,50))

additions=lambda *args:sum(args)
print(additions(10,20))

max_nums=lambda *args:max(args)
print(max_nums(10,2,3,4,5))