import unittest
from Database import Database
from Transaction import Transaction
from Stock import Stock
from constants import BuyTransaction, SellTransaction
from datetime import datetime
from custom_exceptions.NoResultsException import NoResultsException as nr


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testDatabase = Database()
        self.testTransaction = Transaction("test", datetime.now(), BuyTransaction(), 35.00, 10)

    def tearDown(self):
        del self.testDatabase
        del self.testTransaction

    def test_get_stock_id(self):
        stockid_to_add = self.testDatabase.create_new_stock("teststock")
        itemtotest = self.testDatabase.get_stock("teststock")
        self.assertEqual(self.testDatabase.get_stock_id("teststock"), itemtotest.stock_id)

    def test_wrong_argument_in_get_stock_id(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_stock_id(5)

    def test_no_results_in_get_stock_id(self):
        with self.assertRaises(nr):
            self.testDatabase.get_stock_id("ian")

    def test_get_stock(self):
        pass

    def test_wrong_parameter_get_stock(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_stock(5)

    def test_get_stock_with_no_saved_transactions(self):
        pass

    def test_create_new_stock(self):
        self.testDatabase.create_new_stock("testfile")
        stock_to_test = self.testDatabase.get_stock("testfile")
        self.assertEqual(stock_to_test.symbol, "testfile")

    def test_wrong_argument_create_new_stock(self):
        with self.assertRaises(ValueError):
            self.testDatabase.create_new_stock(5)

    def test_save_transaction(self):
        pass

    def test_wrong_arguemnt_save_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.save_transaction(Stock("test"))

    def test_return_value_save_transaction(self):
        pass

    def test_get_transaction(self):
        pass

    def test_wrong_input_get_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_transactions(5)

    def test_delete_transaction(self):
        pass

    def test_wrong_argument_delete_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.delete_transactions("test")


if __name__ == '__main__':
    unittest.main()
