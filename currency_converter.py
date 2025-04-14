
from requests import get
from pprint import PrettyPrinter

API_KEY = "fca_live_KQ5v6GKFt51dWupfoMjK8STd4FenEV5zInY7heCs"
URL = "https://api.freecurrencyapi.com/v1/latest"
printer  = PrettyPrinter()

def get_currencies(*currencies):
    PARAMS= {'apikey': API_KEY, 'base_currency': 'USD', 'currencies': ",".join(currencies)}
    response = get(url=URL, params=PARAMS)
    data = response.json()
    if len(data) == 0:
        print("Invalid currencies")
        return
    return list(data.values())[0]



def main():
    
    currencies = get_currencies('USD', 'EUR')
    print(f"The exchange rate is {currencies['EUR']}")


if __name__ == "__main__":
    main()