# ==================1=======================
# lst=[]
# i=0
# while i<3:
#     name=input("enter the names of three people: ")
#     lst.append(name)
#     i+=1
# c=input("Do you want to add another yes/no: ")
# while c=="yes":
#     name=input("enter name of that person: ")
#     lst.append(name)
#     c=input("Do you want to add another yes/no: ") 
# print(lst)

# =====================2=============================
# lst=[]
# i=0
# while i<3:
#     name=input("enter the names of three people: ")
#     lst.append(name)
#     i+=1
# c=input("Do you want to add another yes/no: ")
# while c=="yes":
#     name=input("enter name of the person: ")
#     lst.append(name)
#     c=input("Do you want to add another yes/no: ") 
# print(lst) 

# n=input("enter any one name from above list: ")
# i=lst.index(n)
# print(i)
    
# r=input("Do you still want that person to come to  the party yes/no:")
# if r=="no":
#     lst.pop(i)
#     print(lst)
# else:
#     print(lst)
# ====================4===================================
# lst=[]
# i=0
# while i<4:
#     name=input("Enter the name: ") 
#     age=input("Enter the age: ")
#     id=input("Enter id: ")
#     lst.append({"name":name,"age":age,"id":id})
#     i+=1
# print(lst)
# s=input("Enter the name of a person from list: ")
# for i in lst:
#     if i["name"]==s:
#         print(f"age:{i['age']},id:{i['id']}")

# # =========================5======================================
# lst=[]
# i=0
# while i<4:
#     name=input("Enter the name: ") 
#     age=input("Enter the age: ")
#     id=input("Enter id: ")
#     lst.append({"name":name,"age":age,"id":id})
#     i+=1

# for i in lst:
#     print(f"name:{i['name']},age:{i['age']}")
# # ================================6=====================================
# booklist={
#     "Walking With Giants":{"author":"G. Ramachandran","publication year":2020,"genre":"mystery"},
#     "One Life is Not Enough":{"author":"Natwar Singh","publication year":2023,"genre":"Action"},
# }

# new={"True Colours":{"author":"Adam Gilchrist","publication year":2003,"genre":"comedy"}}
# booklist.update(new)
# print("New book added: ",booklist,"\n")

# for k,v in booklist.items():
#     if k=="Walking With Giants":
#         v["author"]="Neel Mukherjee"
# print("Author updated: ",booklist,"\n")

# def yearcount(years,date):
#     count = 0
#     for y in years:
#         if y < date:
#             count += 1
#     return count

# years=[]
# for b,v in booklist.items():
#     years.append(v["publication year"])
# count=yearcount(years,2020)
# print("Books that published before 2020: ",count)        
