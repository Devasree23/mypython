items=[
    [1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]
 
    
]
# total number products
# print in stock product names
# print out of stock product names
# print veg category product names
# product available in range of 50-100
# veg products available in range of 40-80

print(len(items),"number of products")

print()
print("product names")
for veg in items:
    print(veg[1])

product_names=[veg[1] for veg in items]
print(product_names)    

instock_names=[veg[1] for veg in items if veg[4]!=0]
print(instock_names)    

outstock_names=[veg[1] for veg in items if veg[4]==0]
print(outstock_names)    

vegetable=[vege[1] for vege in items if vege[3]=="veg"]
print(vegetable) 

product=[vege[1] for vege in items if vege[2]<50 and vege[2]>100]
print(product) 
#or\
product=[item[1] for item in items if item[2] in range(50,100)]
print(product)


veg_product_filter=[item[1] for item in items if item[2] in range(40,80) and item[-2]=="veg"]
print(veg_product_filter)

