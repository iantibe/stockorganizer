from abc import ABC, abstractmethod

DATABASENAME = "stock_database"

class Trantype(ABC):
    @abstractmethod
    def tran_type(self):
        pass


class SellTransaction(Trantype):
    def tran_type(self):
        return "Sell"


class BuyTransaction(Trantype):
    def tran_type(self):
        return "Buy"
