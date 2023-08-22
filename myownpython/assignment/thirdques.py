# ==================first_question=========================
# for i in range(1500,2701):
#     if i%5==0 and i%7==0:
#         print(i)
# ===================second_qusetion=========================

# farenheit=1
# celsius=2
# num=int(input("enter the choice 1 or 2:"))

# if(num==1):
#     temp=int(input("enter the temperature:"))
#     fh=(temp*(9/5))+32
#     print(fh)
# else:
#     fh=int(input("enter the farenheit:"))
#     c=(fh-32)*5/9
#     print(c)    

# =================third_question=============================

# import re

# rule = r"[A-Z][a-z]{13}[@$#][0-9]"
# password = input("enter the password:")
# matcher = re.fullmatch(rule, password)

# if matcher is None:
#     print("invalid")
# else:
#     print("valid")

# ==================fourth_question===========================
# import math

# a = int(input("enter the side of triangle a:"))
# b = int(input("enter the side of triangle b:"))
# c = int(input("enter the side of triangle c:"))

# if a == b == c:
#     print("Equilateral triangle")
#     area = (math.sqrt(3) / 4) * a**2
#     print("Area:", area)
#     perimeter = 3 * a
#     print("Perimeter:", perimeter)
# elif a == b or a == c or b == c:
#     print("Isosceles triangle")
#     area = (1 / 2) * b * math.sqrt(a**2 - (b**2 / 4))
#     print("Area:", area)
#     perimeter = 2 * a + b
#     print("Perimeter:", perimeter)
# else:
#     print("Scalene triangle")
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     print("Area:", area)
#     perimeter = a + b + c
#     print("Perimeter:", perimeter)

# ======================fifth_question==========================

# yes=1
# no=0
# num=int(input("enter 1 is yes and 0 is no,if there is Raining:"))

# if(num==1):
#     q2=int(input("enter 1 is yes and 0 is no,if there is windy:"))
#     if(q2==1):
#         print("its too windy for an umbrella")
#     else:
#         print("take umbrella")   
# else:
#     print("enjoy your day")    

# ==========================sixth_question========================
# square=1
# triangle=2

# num=int(input("enter the 1 or 2:"))
# if num ==1:
#     print("You chose square.")
#     side=int(input("enter the length of the side of square:"))
#     area=side**2
#     print(area)
# elif(num==2):
#     print("You chose triangle.")
#     base=int(input("enter the length of the base of triangle:"))
#     height=int(input("enter the length of the height of triangle:"))
#     area=(base*height)/2
#     print(area)
# else:
#     print("number not exist")    

# ======================seventh_question==========================

# lst=[1,2,2,3,3,4,6,7,88,99,]
# li=[]
# for i in range(0,len(lst)-1):
#     if lst[i]==lst[i+1]:
#         li.append(lst[i])
# print(li)    

# =======================eight_question=============================

# age=int(input("enter your age:"))
# if age>=18:
#     print("you can vote")
# elif age==17:
#     print("you can learn driving")
# elif age==16:
#     print("you can buy a lottery ticket")
# elif age<16:
#     print("you can go for a treat")

# ===================ninth_question====================================
# def invite_people():
#     num_people = int(input("How many people do you want to invite to the party? "))

#     if num_people < 10:
#         names = []
#         for i in range(num_people):
#             name = input(f"Enter the name of person {i+1}: ")
#             names.append(name)
#             print(f"{name} has been invited.")
#     else:
#         print("Too many people.")

# invite_people()
# ===================10thquestion=======================================
# def main():
#     user_input = input("Please enter 1, 2, or 3: ")

#     if user_input == '1':
#         print("Thank you")
#     elif user_input == '2':
#         print("Well done")
#     elif user_input == '3':
#         print("Correct")
#     else:
#         print("Error message")

# if _name_ == "_main_":
#     main()
    
    



