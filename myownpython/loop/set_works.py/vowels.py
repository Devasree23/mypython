word="pnemonoultramicroscopicsilicovolcaniosis"
vowel_list=["a","e","i","o","u"]
v_count=0
c_count=0
for ch in word:
    if ch in vowel_list:
        v_count+=1
    else:
        c_count+=1    
print(f"vowels count {v_count} and concenants count {c_count}")        
    