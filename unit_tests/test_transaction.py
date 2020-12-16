"""
Name of program: test_transaction.py
Author: Ian Tibe
Date of last modification: 12/16/2020

Unit test for Transaction class
"""
import unittest
from Transaction import Transaction
from datetime import datetime
from constants import BuyTransaction


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test = Transaction("test", datetime.now(), BuyTransaction(), 35.00, 10)

    def tearDown(self):
        del self.test

    def test_create_object(self):
        self.assertEqual(self.test.number_of_shares, 10)

    def test_get_text_of_tran_type(self):
        self.assertEqual(self.test.get_text_of_tran_type(), BuyTransaction().tran_type())

    def test_invalid_tran_type(self):
        with self.assertRaises(ValueError):
            Transaction("Test", datetime.now(), "Invalid", 36, 25)

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            Transaction("test", "invalid", BuyTransaction(), 36.01, 25)

    def test_invalid_shares(self):
        with self.assertRaises(ValueError):
            Transaction("Test", datetime.now(), BuyTransaction(), 25.36, "Invalid")

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Transaction("test", datetime.now(), BuyTransaction(), "invalid", 10)


if __name__ == '__main__':
    unittest.main()
