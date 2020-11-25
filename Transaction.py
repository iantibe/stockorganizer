from datetime import datetime

class Transaction:

    def __init__(self, symbol, date, action, price, number_of_shares):
        self.symbol = str(symbol)
        self.date = date
        self.action = action
        self.price = float(price)
        self.number_of_shares = int(number_of_shares)

