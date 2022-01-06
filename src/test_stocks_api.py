"""Please let this work"""
import unittest
import unittest.mock
from stocks_api import get_stocks


class TestStocksApi(unittest.TestCase):
    """Unit Tests for the stock api"""

    def test_stocks_api_response(self):
        """This test makes sure the info getting pulled down contains the expected values"""
        self.assertIn("name", str(get_stocks("Voo")))


if __name__ == "__main__":
    unittest.main()
