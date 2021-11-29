import json
import os 
import requests
import pandas as pd

def get_stocks(stocks):
    url = 'https://api.stockdata.org/v1/data/quote'
    stock_api_key = os.environ['STOCK']
    parameters = {
        'symbols' : stocks,
        'api_token' : stock_api_key
    }

    s = requests.Session()
    r = s.get(url, params=parameters)

    json_response = r.json()['data']
    # return pd.DataFrame(json_response)
    return r.json()['data'][0]['name']

if __name__ == "__main__":
    print(get_stocks('VOO'))



