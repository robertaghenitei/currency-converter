
from requests import get
from pprint import PrettyPrinter

API_KEY = "fca_live_KQ5v6GKFt51dWupfoMjK8STd4FenEV5zInY7heCs"
URL = "https://api.freecurrencyapi.com/v1/latest"
printer  = PrettyPrinter()

def get_currencies(*currencies):
    PARAMS= {'apikey': API_KEY, 'base_currency': 'USD', 'currencies': ",".join(currencies)}
    response = get(url=URL, params=PARAMS)

    if response.status_code != 200:
        print("There was a problem with fetching the data.", response.status_code)
        return
    

    data = response.json()
    if len(data) == 0:
        print("Invalid currencies")
        return
    return list(data.values())[0]



def main():
    currency = input("Chose a currency to convert to dollar: ")
    currencies = get_currencies('USD', currency)
    
    if currencies and currency in currencies:
        print(f"The exchange rate is {currencies[currency]}")
    else:
        print("No such currency or API error")

if __name__ == "__main__":
    main()