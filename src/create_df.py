import pandas as pd


def create_df(data):
    df = pd.DataFrame(data)
    custom_df = df[
        ["name", "price", "day_high", "day_low", "52_week_high", "52_week_low"]
    ]
    return custom_df
