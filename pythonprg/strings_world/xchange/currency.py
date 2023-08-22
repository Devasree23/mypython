# from json import load
# with open("C:\\Users\\vaisa\\OneDrive\\Desktop\\pythonprg\\strings_world\\xchange\\data.json","r",encoding="UTF-8") as f:
#     data=load(f)
rates = {"USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.7974,
    "INR": 82.0914
}
amount=int(input("enter the amount>"))
fromCurrencyCode=input("enter source currency code>")
toCurrencyCode=input("enter source currency code>")

# eqn=(amount/rate_fromCurrencyCode)*rate_toCurrencyCode---------
rate_fromCurrencycode=rates.get(fromCurrencyCode)
rate_toCurrencyCode=rates.get(toCurrencyCode)

result=(amount/rate_fromCurrencycode)*rate_toCurrencyCode
print(result)