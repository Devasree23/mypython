print("enter the year:")    
year=2100  
print("check the year is leap year or not")  
# if(year%4==0):
#     print(year, "is leap yr")  
# else:
#     print(year,"is not leap yr")
# is_leapyear=False

# if(year%4==0):
#     is_leapyear=True
# elif(year%400==0):
#     is_leapyear=True
# elif(year%100!=0):
#     is_leapyear=False

# print(year,"is leap year",is_leapyear)            


year=2200
if(((year%4==0) or(year%400==0))and(year%100!=0)):
    print(year,"is leap year")
else:
    print(year,"is not leap year")  

    