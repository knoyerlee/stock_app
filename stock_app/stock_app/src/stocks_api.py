import os 
import requests

def get_stocks(stocks):
    stocks = stocks.strip().replace(" ", "")
    url = 'https://api.stockdata.org/v1/data/quote'
    stock_api_key = os.environ['STOCK']
    parameters = {
        'symbols' : stocks,
        'api_token' : stock_api_key
    }

    s = requests.Session()
    r = s.get(url, params=parameters)

    json_response = r.json()['data']

    return json_response



