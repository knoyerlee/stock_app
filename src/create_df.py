"""This creates a pandas df for us"""
import pandas as pd


def create_df(data):
    """This function takes data from the stock api and creates a dataframe out of it"""
    new_dataframe = pd.DataFrame(data)
    custom_df = new_dataframe[
        ["name", "price", "day_high", "day_low", "52_week_high", "52_week_low"]
    ]
    return custom_df
