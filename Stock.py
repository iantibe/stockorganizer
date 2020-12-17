"""
Name of Program: Stock.py
Author: Ian Tibe
Date of last modification: 12/16/2020

Stock class definition
"""
from constants import SellTransaction, BuyTransaction, Trantype
from Transaction import Transaction


class Stock:
    """
    Stock class definition
    """
    def __init__(self, symbol, trans=None):
        """
        Constructor
        :param symbol: String of stock symbol
        :param trans: list of transactions
        """
        self.symbol = str(symbol)
        if trans is None:
            self.transactions = []
        else:
            if isinstance(trans, list):
                for x in trans:
                    if not isinstance(x, Transaction):
                        raise ValueError("Transaction list contains wrong class type")
                self.transactions = trans
            else:
                raise ValueError("Transaction item is not in a list")
        self.stock_id = None
        self.last_price_update = None
        self.last_price = None

    def add_transactions(self, tran):
        """
        Adds a transaction to the stock
        :param tran: Transaction object
        :return: None
        """
        if isinstance(tran, Transaction):
            self.transactions.append(tran)
        else:
            raise ValueError("Input must be type Transaction")

    def calculate_current_shares(self):
        """
        Calculates current owned shares
        :return: Integer of number of shares of stock owned
        """
        if len(self.transactions) == 0:
            return 0
        total = 0

        buyType = BuyTransaction()
        sellType = SellTransaction()

        for x in self.transactions:
            if x.get_text_of_tran_type() == buyType.tran_type():
                total += x.number_of_shares
            if x.get_text_of_tran_type() == sellType.tran_type():
                total -= x.number_of_shares
        return total

    def calculate_buy_or_sell_total_price(self, operation):
        """
        Calculates total buy or sell price of stock
        :param operation: Trantype of object to identify type of transaction
        :return: float of buy or sell price
        """
        if isinstance(operation, Trantype):
            if len(self.transactions) == 0:
                return 0
            total = 0
            for x in self.transactions:
                if x.get_text_of_tran_type() == operation.tran_type():
                    total += x.price * x.number_of_shares
            return total

        else:
            raise ValueError("Invalid operation variable")

