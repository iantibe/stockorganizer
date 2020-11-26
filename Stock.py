from constants import SellTransaction,BuyTransaction
from Transaction import Transaction

class Stock:

    def __init__(self, symbol, trans=None):
        self.symbol = str(symbol)
        if trans is None:
            self.transactions = []
        else:
            if isinstance(trans, list):

                self.transactions = trans
            else:
                raise ValueError("Transaction item is not in a list")
        self.stock_id = None

    def add_transactions(self, tran):
        if isinstance(tran, Transaction):
            self.transactions.append(tran)
        else:
            raise ValueError("Input must be type Transaction")

    def calculate_current_shares(self):
        pass
