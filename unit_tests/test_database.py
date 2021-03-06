"""
Name of Program: test_database.py
Author: Ian Tibe
Date of last modification: 12/16/2020

Unit tests for Database class
"""
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
        self.testDatabase.create_new_stock("teststock")
        itemtotest = self.testDatabase.get_stock("teststock")
        self.assertEqual(self.testDatabase.get_stock_id("teststock"), itemtotest.stock_id)

    def test_wrong_argument_in_get_stock_id(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_stock_id(5)

    def test_no_results_in_get_stock_id(self):
        with self.assertRaises(nr):
            self.testDatabase.get_stock_id("ian")

    def test_get_stock(self):
        self.testDatabase.create_new_stock("test_get_stock")
        testStock = self.testDatabase.get_stock("test_get_stock")
        self.assertEqual(testStock.symbol, "test_get_stock")

    def test_wrong_parameter_get_stock(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_stock(5)

    def test_get_stock_with_no_saved_transactions(self):
        self.testDatabase.create_new_stock("test_get_stock_with_no_saved_transactions")
        testStock = self.testDatabase.get_stock("test_get_stock_with_no_saved_transactions")
        self.assertEqual(len(testStock.transactions), 0)

    def test_create_new_stock(self):
        self.testDatabase.create_new_stock("testfile")
        stock_to_test = self.testDatabase.get_stock("testfile")
        self.assertEqual(stock_to_test.symbol, "testfile")

    def test_wrong_argument_create_new_stock(self):
        with self.assertRaises(ValueError):
            self.testDatabase.create_new_stock(5)

    def test_save_transaction(self):
        self.testDatabase.create_new_stock("save_tran")
        self.testDatabase.save_transaction(Transaction("save_tran",  datetime.strptime("2020-5-20 0:0:0", "%Y-%m-%d %H:%M:%S"),BuyTransaction(), 12, 5))
        item = self.testDatabase.get_transactions("save_tran")
        self.assertEqual(item[0].symbol, "save_tran")

    def test_wrong_arguemnt_save_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.save_transaction(Stock("test"))

    def test_get_transaction(self):
        self.testDatabase.create_new_stock("testtran")
        self.testDatabase.save_transaction(Transaction("testtran",  datetime.strptime("2020-5-20 0:0:0", "%Y-%m-%d %H:%M:%S"),BuyTransaction(), 12, 5))
        item = self.testDatabase.get_transactions("testtran")
        self.assertEqual(item[0].symbol, "testtran")
    def test_wrong_input_get_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.get_transactions(5)

    def test_delete_transaction(self):
        self.testDatabase.create_new_stock("testdelete")
        self.testDatabase.save_transaction(Transaction("testdelete", datetime.strptime("2020-5-20 0:0:0", "%Y-%m-%d %H:%M:%S"), BuyTransaction(), 12, 5))
        self.testDatabase.delete_transactions(Transaction("testdelete", datetime.strptime("2020-5-20 0:0:0", "%Y-%m-%d %H:%M:%S"), BuyTransaction(), 12, 5))
        with self.assertRaises(nr):
            item = self.testDatabase.get_transactions("testdelete")

    def test_wrong_argument_delete_transaction(self):
        with self.assertRaises(ValueError):
            self.testDatabase.delete_transactions("test")

    def test_get_all_stocks(self):
        self.testDatabase.create_new_stock("test")
        group_of_stocks = self.testDatabase.get_all_stocks()
        self.assertTrue(len(group_of_stocks) >= 1)

    def test_delete_individual_transaction_using_primary_key(self):
        self.testDatabase.create_new_stock("testpk")
        self.testDatabase.save_transaction(Transaction("testpk", datetime.strptime("2020-5-20 0:0:0", "%Y-%m-%d %H:%M:%S"), BuyTransaction(), 12, 5))
        item = self.testDatabase.get_transactions("testpk")
        self.testDatabase.delete_individual_transaction_using_primary_key(item[0].tran_id)
        with self.assertRaises(nr):
            self.testDatabase.get_transactions("testpk")

    def test_wrong_argument_delete_individual_transaction_using_primary_key(self):
        with self.assertRaises(ValueError):
            self.testDatabase.delete_individual_transaction_using_primary_key("a")


if __name__ == '__main__':
    unittest.main()
