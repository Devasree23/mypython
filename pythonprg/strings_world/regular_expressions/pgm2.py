import re
resi=input("enter the residence code: ")
ekm=re.search("^0484",resi)
ijk=re.search("^0480",resi)
tcr=re.search("^0487",resi)
mpr=re.search("^0494",resi)
ksd=re.search("^04994",resi)
cct=re.search("^0495",resi)
if ekm:
    print("ekm")
elif ijk:
    print("ijk")  
elif tcr:
    print("tcr")
elif mpr:
    print("mpr") 
if ksd:
    print("ksd") 
if cct:
    print("cct")                


