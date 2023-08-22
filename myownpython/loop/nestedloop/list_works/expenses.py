expenses=[20000,200,300,100000,300]

#print all expenses
for exp in expenses:
    print(exp)
for exp in expenses:
    if exp>16000 :
        print(f"expense greater than 16000={exp}")   

print()

max_exp=max(expenses)
print(max_exp)

min_exp=min(expenses)
print(min_exp)

total_exp=sum(expenses)
print(total_exp)