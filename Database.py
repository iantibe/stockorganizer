import constants
import sqlite3
from sqlite3 import Error
from Transaction import Transaction
from Stock import Stock
from constants import BuyTransaction, SellTransaction
from datetime import datetime

class Database:
    def __init__(self):
        self.create_tables()

    def __init_connection(self):
        try:
            connection = sqlite3.connect(constants.DATABASENAME)
            return connection
        except Error:
            raise Error

    def create_tables(self):

        sql_portfolio = """create table if not exists portfolio (
                        id integer primary key, 
                        stock text not null);"""

        sql_transaction = """create table if not exists transactions (
                              id integer primary key,
                              stock_id integer not null,
                              date text not null,
                              number_of_shares real not null,
                              price_per_share real not null,
                              transaction_type text not null,
                              FOREIGN KEY (stock_id) REFERENCES portfolio (id));"""

        try:
            con = self.__init_connection()
            dataset = con.cursor()
            dataset.execute(sql_portfolio)
            dataset.execute(sql_transaction)
            con.close()
        except Error:
            print(Error.with_traceback())
        finally:
            con.close()

    def get_stock(self, symbol):
        pass

    def create_new_stock(self, symbol):
        if not isinstance(symbol, str):
            raise ValueError
        try:
            listofitems = []
            listofitems.append(symbol)

            sql_statement = """INSERT INTO portfolio(stock)
                               VALUES (?);"""
            conn = self.__init_connection()
            dataset = conn.cursor()
            dataset.execute(sql_statement, listofitems)
            conn.commit()
            conn.close()
            return dataset.lastrowid
        except Error:
            print(Error)
        finally:
            conn.close()

    def save_transaction(self, tran):
        if not isinstance(tran, Transaction):
            raise ValueError
        try:
            listofitems = []
            stock = Stock(tran.symbol)
            stock_id = self.get_stock_id(stock)

            listofitems.append(stock_id)
            listofitems.append(tran.date)
            listofitems.append(tran.number_of_shares)
            listofitems.append(tran.price)
            listofitems.append(tran.action.tran_type())

            sql_statement = """INSERT INTO transactions(stock_id, date, number_of_shares, 
                                price_per_share, transaction_type)
                                VALUES (?, ?, ?, ?, ?);"""
            conn = self.__init_connection()
            dataset = conn.cursor()
            dataset.execute(sql_statement, listofitems)
            conn.commit()
            conn.close()
            return dataset.lastrowid
        except Error:
            print(Error)
        finally:
            conn.close()

    def get_stock_id(self, stock):
        if not isinstance(stock, Stock):
            raise ValueError("Invalid input argument, Must Be Stock object")
        try:
            argument_list = []
            argument_list.append(stock.symbol)
            sql_command = """select id from portfolio
                            where stock = ?"""
            conn = self.__init_connection()
            dataset = conn.cursor()
            dataset.execute(sql_command, argument_list)
            rows = dataset.fetchall()
            for x in rows:
                return x[0]
        except Error:
            print(Error)
        finally:
            conn.close()


if __name__ == '__main__':
    test = Database()
    tran = Transaction("nyse", datetime.now(), BuyTransaction(), 25.26, 25)
    print(test.save_transaction(tran))
