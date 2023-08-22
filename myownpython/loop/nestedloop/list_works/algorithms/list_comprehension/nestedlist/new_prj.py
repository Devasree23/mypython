mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]
#total number of mobiles
print(f"{len(mobiles)},mobiles available")
#print all mobile names
for mob in mobiles:
    print(mob[1])

        
print()  

mobile=[mob[1] for mob in mobiles]
print(mobile)

#print 4g mobile names
for mob in mobiles:
    if (mob[3]=="4g"):
        print(mob[1])

print()  

fourg_mobile=[mob[1] for mob in mobiles if mob[3]=="4g"]

print(fourg_mobile)

#print mobile name price<30000
for mob in mobiles:
    if (mob[2]<30000):
        print(mob[1])
less_than_30000=[mob[1] for mob in mobiles if mob[2]<30000]
print(less_than_30000)        

#print mobile names available in range of 30000 to 50000
# for mob in mobiles:
#     if (mob[2]>30000 and mob[2]<50000):
#         print(mob[1])
price_filter=[mob[1] for mob in mobiles if mob[2] in range(30000,50000)]  
print(price_filter)      
#print 5g mobile names available under 25000
mobile_names=[mob[1] for mob in mobiles if mob[2]<25000 and mob[3]=="5g"]
print(mobile_names)
