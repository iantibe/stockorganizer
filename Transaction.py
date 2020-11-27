from datetime import datetime
from constants import Trantype


class Transaction:
    def __init__(self, symbol, date, action, price, number_of_shares):
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
        return self.action.tran_type()
