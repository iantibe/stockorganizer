from abc import ABC, abstractmethod

DATABASENAME = "stock_database"
API_KEY = "0S5TK5I9Z6K65PMB"
API_ERROR_MESSAGE = "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY."

def generate_url(symbol):
    if isinstance(symbol, str):
        return "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=1min&apikey=" + API_KEY
    else:
        raise ValueError("wrong data type for stock symbol")


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
