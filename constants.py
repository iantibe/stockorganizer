"""
Program Name: constants.py
Author: Ian Tibe
Date of last modification: 12/16/2020

File contains constants, classes, and methods that are used through out the program
"""
from abc import ABC, abstractmethod

# Program name
PROGRAM_NAME = "Stock Organizer"

# Name of database file
DATABASENAME = "stock_database"

# Key provided by api to access api
API_KEY = "0S5TK5I9Z6K65PMB"

# Api error response
API_ERROR_MESSAGE = {"Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY."}

# Spacer between fields in stock main window
STOCK_WINDOW_SPACE_BETWEEN_FIELDS = "                          "


def generate_url(symbol):
    """
    Generates url with stock symbol to get quote
    :param symbol: string of stock ticker symbol
    :return: Url to retrieve given stock quote
    """
    if isinstance(symbol, str):
        return "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=1min&apikey=" + API_KEY
    else:
        raise ValueError("wrong data type for stock symbol")


class Trantype(ABC):
    """
    Define Transaction type abstract method
    """
    @abstractmethod
    def tran_type(self):
        pass


class SellTransaction(Trantype):
    """
    Sell Transaction class
    """
    def tran_type(self):
        """
        Gets tran type
        :return: Tran type string
        """
        return "Sell"


class BuyTransaction(Trantype):
    """
    Buy Transaction class
    """
    def tran_type(self):
        """
        gets tran type
        :return: tran type string
        """
        return "Buy"
