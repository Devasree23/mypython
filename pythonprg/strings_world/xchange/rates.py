from json import load
with open("C:\\Users\\vaisa\\OneDrive\\Desktop\\pythonprg\\strings_world\\xchange\\data.json","r",encoding="UTF-8") as f:
    data=load(f)
print(data)
rates=data.get("conversion_rates")
amount=int(input("enter the amount>"))
fromCurrencyCode=input("enter source currency code>")
toCurrencyCode=input("enter source currency code>")

rate_fromCurrencycode=rates.get(fromCurrencyCode)
rate_toCurrencyCode=rates.get(toCurrencyCode)

result=(amount/rate_fromCurrencycode)*rate_toCurrencyCode
print(result)