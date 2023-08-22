st={3,2,True,4,5}
print(st)
print(type(st))
for item in st:
    print(item)
# print(dir(st))
st.add(33)
print(st)

lst=[1,2,3,4,5]
st=set(lst)
print(st)

s1={1,2,3,4,5,7}
s2={3,6,7,8,9,10}
union_set=s1.union(s2)
print(union_set)
intersect_set=s1.intersection(s2)
print(intersect_set)
difference_set=s1.difference(s2)
print(difference_set)



