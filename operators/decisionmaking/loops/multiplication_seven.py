num=7
for i in range(1,13):
    print(f"{i}*{num}={num*i}")
print()
print()
print("print all multiples of seven in between 1 to 100")
print()
for i in range(1,101):
    if(i%7==0):
        print(i)

print()
print()

print("u can select a range of 10 numbers,check whether the number is divisible by 9 ,if divisible by 9 then the result should be number multiplied by 9")

for j in range(40,51):
    if(j%9==0):
        print(j*9)
