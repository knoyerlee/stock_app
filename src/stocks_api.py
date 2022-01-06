"""This hits a stock api and returns some kind of data"""
import os
import requests


def get_stocks(stocks):
    """This function hits a stock api and returns a response.
    Response is based on the ticker that is fed into it"""
    stocks = stocks.strip().replace(" ", "")
    url = "https://api.stockdata.org/v1/data/quote"
    # This env is in .bashrc
    stock_api_key = os.environ["STOCKAPPTOKEN"]
    parameters = {"symbols": stocks, "api_token": stock_api_key}

    our_session = requests.Session()
    our_response = our_session.get(url, params=parameters)

    json_response = our_response.json()["data"]

    return json_response
