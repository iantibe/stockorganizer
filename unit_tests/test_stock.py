import unittest
from Stock import Stock
from Transaction import Transaction
from constants import BuyTransaction, SellTransaction
from datetime import datetime

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.now = datetime.now()
        self.buy = BuyTransaction()
        self.testTran = Transaction("IBM", self.now, self.buy, 115.00, 10)

    def tearDown(self):
        del self.now
        del self.buy
        del self.testTran

    def test_create_object(self):
        testObj = Stock("IBM")
        self.assertEqual(testObj.symbol, "IBM")

    def test_create_object_with_tran(self):
        listOfTran = []
        listOfTran.append(self.testTran)
        testObj = Stock("IBM", listOfTran)
        self.assertEqual(testObj.transactions.pop(), self.testTran)

    def test_transaction_not_list_format(self):
        with self.assertRaises(ValueError):
            Stock("IBM", self.testTran)

    def test_add_transaction_after_Stock_Object_creation(self):
        second_transaction = Transaction("Google", datetime.now(), self.buy,36.23,10)
        listOfTran = []
        listOfTran.append(self.testTran)
        testObj = Stock("IBM", listOfTran)
        testObj.add_transactions(second_transaction)
        self.assertEqual(len(testObj.transactions), 2)

if __name__ == '__main__':
    unittest.main()
