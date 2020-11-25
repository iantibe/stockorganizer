class Stock:

    def __init__(self, symbol, trans=None):
        self.symbol = str(symbol)
        if trans is None:
            self.transactions = []
        self.stock_id = None

    def add_transactions(self, tran):
        self.transactions.append(tran)

    def calculate_current_shares(self):
        pass
