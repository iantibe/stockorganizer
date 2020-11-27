import unittest
from Stock import Stock
from Transaction import Transaction
from constants import BuyTransaction, SellTransaction
from datetime import datetime

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.now = datetime.now()
        self.buy = BuyTransaction()
        self.sell = SellTransaction()
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

    def test_wrong_object_type_in_transactions_list(self):
        tranItem1 = Transaction("Google", datetime.now(), self.buy, 23.32, 20)
        tranItem2 = "WrongObject"

        listOfTrans = []
        listOfTrans.append(tranItem1)
        listOfTrans.append(tranItem2)

        with self.assertRaises(ValueError):
            testObj = Stock("Google", listOfTrans)

    def test_wrong_object_type_added_to_excisting_object(self):
        tranItem1 = Transaction("Google", datetime.now(), self.buy, 23.32, 20)
        tranItem2 = "WrongObject"

        listOfTrans = []
        listOfTrans.append(tranItem1)
        testObj = Stock("Google", listOfTrans)

        with self.assertRaises(ValueError):
            testObj.add_transactions(tranItem2)

    def test_calculate_total_shares_non_zero_number_of_transactions(self):
        tranItem1 = Transaction("Google", datetime.now(), self.buy, 23.32, 20)
        tranItem2 = Transaction("IBM", datetime.now(), self.buy,23.36, 20)
        tranItem3 = Transaction("FaceBook", datetime.now(), self.sell, 23.36, 10)
        tranItem4 = Transaction("Apple", datetime.now(), self.sell, 36.23 , 10)

        listOfTrans = []
        listOfTrans.append(tranItem1)
        listOfTrans.append(tranItem2)
        listOfTrans.append(tranItem3)
        listOfTrans.append(tranItem4)

        testObj = Stock("Test", listOfTrans)

        self.assertEqual(testObj.calculate_current_shares(), 20)

    def test_calculate_total_shares_zero_number_of_transactions(self):
        testObj = Stock("Test")
        self.assertEqual(testObj.calculate_current_shares(), 0)

    def test_calculate_buy_and_price(self):
        tranItem1 = Transaction("Google", datetime.now(), self.buy, 20.00, 20)
        tranItem2 = Transaction("IBM", datetime.now(), self.buy, 80.00, 20)
        tranItem3 = Transaction("FaceBook", datetime.now(), self.sell, 10.00, 10)
        tranItem4 = Transaction("Apple", datetime.now(), self.sell, 40.00, 10)

        listOfTrans = []
        listOfTrans.append(tranItem1)
        listOfTrans.append(tranItem2)
        listOfTrans.append(tranItem3)
        listOfTrans.append(tranItem4)

        testObj = Stock("Test", listOfTrans)

        self.assertEqual(testObj.calculate_buy_or_sell_total_price(BuyTransaction()), 100)
        self.assertEqual(testObj.calculate_buy_or_sell_total_price(SellTransaction()), 50)

    def test_zero_calculate_buy_or_sell_price(self):
        testObj = Stock("test")
        self.assertEqual(testObj.calculate_buy_or_sell_total_price(BuyTransaction()), 0)
        self.assertEqual(testObj.calculate_buy_or_sell_total_price(SellTransaction()), 0)

    def test_invalid_operation_parameter_for_calculate_price(self):
        testObj = Stock("test")
        with self.assertRaises(ValueError):
            testObj.calculate_buy_or_sell_total_price("test")

if __name__ == '__main__':
    unittest.main()
