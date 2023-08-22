sen="michu is a cute kitten"
words=sen.split(" ")
print(sen.startswith("michu"))
if words[0]=="michu":
    print("the sentence startswith the name michu")
# ============================================
bol=sen.startswith("michu")
print(bol)
if bol==True:
    print("the sentence startswith the name michu")
# ==================================================
import re
sen="michu is a cute kitten"
x=re.search("^michu",sen)
print(x) 
# ===================================================
import re
sen="michu is a cute kitten"
en=re.search("kitten$",sen)
print(en)   
# =================================================
sen2="michu is a cute kitten "
st_en=re.search("^michu.*kitten$",sen)
print(st_en)
st_en=re.search("^michu.*kitten$",sen2)
print(st_en)