allusers=["mohanlal","asif","fahad","dq","vijay","nivin"]
dq_friendlist=["mohanlal","fahad","asif"]
suggestion=set(allusers).difference(set(dq_friendlist))
suggestion.remove("dq")
print(suggestion)

asif_friendlist=["mohanlal","fahad","vijay","nivin"]
mutual=set(dq_friendlist).intersection(set(asif_friendlist))
print(mutual)
        