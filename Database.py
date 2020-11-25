import constants
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        pass

    def __init_connection(self):
        try:
            connection = sqlite3.connect(constants.DATABASENAME)
            return connection
        except Error:
            raise Error

    def __create_tables(self):
        pass

    def get_stock(self, symbol):
        pass

    def save_stock(self, symbol):
        pass

    def save_transaction(self, symbol):
        pass

