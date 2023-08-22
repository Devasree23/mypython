from json import load
with open("C:\\Users\\vaisa\\OneDrive\\Desktop\\pythonprg\\strings_world\\restcountries\\rest.json","r",encoding="UTF-8") as f:
    data=load(f)
print(len(data)) 
print("-----------------------------------------------------------------------")

#print all country names
country_names=[c.get("name") for c in data ]
print(country_names)

print("-----------------------------------------------------------------------")
#print all region names
region_names={c.get("region") for c in data}
print(region_names)
print("-----------------------------------------------------------------------")
#print asian country names
asian_country_names=[c.get("name") for c in data if c.get("region")=="Asia"]
print(asian_country_names)
print("-----------------------------------------------------------------------")
#print population of afganisthan
population_afghanisthan=[c.get("population") for c in data if c.get("name")=="Afghanistan"]
print(population_afghanisthan)
print("-----------------------------------------------------------------------")
#print indian borders
indian_borders=[c.get("borders") for c in data if c.get("name")=="India" ][0]
print(indian_borders)
country_border_names=[c.get("name") for c in data if c.get("alpha3Code") in indian_borders]
print(country_border_names)
print("-----------------------------------------------------------------------")
#print india currency code
currency_india=[c.get("currencies") for c in data if c.get("name")=="India"][0]
print(currency_india)
currency_code=[for c in data if c.get()]

