"""Unit tests for the creation of dataframe"""
import unittest
import pandas as pd
from create_df import create_df


class TestCreateDf(unittest.TestCase):
    """Unit tests variable setup"""
    def setUp(self):
        self.stock_data = [
            {
                "ticker": "VOO",
                "name": "Vanguard 500 Index Fund ETF",
                "exchange_short": "NYSEARCA",
                "exchange_long": "NYSE Arca",
                "mic_code": "ARCX",
                "currency": "USD",
                "price": 436.4,
                "day_high": 438.35,
                "day_low": 436.41,
                "day_open": 437.32,
                "52_week_high": 440.36,
                "52_week_low": 335.37,
                "market_cap": None,
                "previous_close_price": 437.79,
                "previous_close_price_time": "2021-12-30T15:59:54.000000",
                "day_change": -0.32,
                "volume": 63168,
                "is_extended_hours_price": False,
                "last_trade_time": "2021-12-31T15:59:46.000000",
            }
        ]
        self.stock_data_formatted = pd.DataFrame(
            [
                {
                    "name": "Vanguard 500 Index Fund ETF",
                    "price": 436.4,
                    "day_high": 438.35,
                    "day_low": 436.41,
                    "52_week_high": 440.36,
                    "52_week_low": 335.37,
                }
            ]
        )

    def test_create_df_positive(self):
        """Actual unit test"""
        created_data = create_df(self.stock_data)
        self.assertEqual(str(self.stock_data_formatted), str(created_data))


if __name__ == "__main__":
    unittest.main()

bad_ex = [
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    1111111111111111111111111111,
    333333333333333333333333333,
]
