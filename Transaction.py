"""
Name of Program: Transaction.py
Author: Ian Tibe
Date of last modification: 12/16/2020

Definition of Transaction Class
"""
from datetime import datetime
from constants import Trantype


class Transaction:
    def __init__(self, symbol, date, action, price, number_of_shares):
        """
        Constructor
        :param symbol: string of stock symbol
        :param date: date object
        :param action: TranType object
        :param price: price
        :param number_of_shares: Integer of shares quantity
        """
        self.symbol = str(symbol)
        if isinstance(date, datetime):
            self.date = date
        else:
            raise ValueError("Invalid Date object")
        if isinstance(action, Trantype):
            self.action = action
        else:
            raise ValueError("Invalid Tranaction Type")
        self.price = float(price)
        self.number_of_shares = int(number_of_shares)
        self.tran_id = -1

    def get_text_of_tran_type(self):
        """
        Gets tran type
        :return: string of tran type
        """
        return self.action.tran_type()
