import unittest
from Api import Api
from Stock import Stock
from datetime import datetime


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.testApi = Api()
        self.testStock = Stock("jnj")

    def tearDown(self):
        del self.testStock
        del self.testApi

    def test_incorrect_stock(self):
        with self.assertRaises(ValueError):
            badStock = Stock("jiok")
            self.testApi.get_stock_quote(badStock)

    def test_no_input_stock(self):
        with self.assertRaises(ValueError):
            badStock = Stock("")
            self.testApi.get_stock_quote(badStock)

    def test_api_call(self):
        test = self.testApi.get_stock_quote(self.testStock)
        self.assertIs(type(test.last_price), float)
        self.assertIs(type(test.last_price_update), datetime)

if __name__ == '__main__':
    unittest.main()
