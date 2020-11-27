import constants
import sqlite3
from sqlite3 import Error
from Transaction import Transaction
from Stock import Stock
from constants import BuyTransaction, SellTransaction
import datetime

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
        try:
            if not isinstance(symbol, str):
                raise ValueError("Parameter is not type string")
            stock_to_return = Stock(symbol)
            tran_list = self.get_transactions(symbol)
            stock_id = self.get_stock_id(stock_to_return)
            stock_to_return.transactions = tran_list
            stock_to_return.stock_id = stock_id
            return stock_to_return
        except Error:
            print(Error.with_traceback())



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

    def get_transactions(self, stock):
        if not isinstance(stock, str):
            raise ValueError("Invalid input parameter. Must be string")
        try:
            stock_to_lookup = Stock(stock)
            stock_id_to_lookup = self.get_stock_id(stock_to_lookup)
            sql_statement = """select p.stock, transactions.id, date, number_of_shares, price_per_share,
                            transaction_type from transactions  inner join portfolio p on p.id = transactions.stock_id 
                            where stock_id = ?"""
            argument_list = []
            argument_list.append(stock_id_to_lookup)
            conn = self.__init_connection()
            dataset = conn.cursor()
            dataset.execute(sql_statement, argument_list)
            rows = dataset.fetchall()
            output = []
            for x in rows:
                time_in_datetime = datetime.datetime.strptime(x[2], "%Y-%m-%d %H:%M:%S.%f")
                if x[5] == SellTransaction().tran_type():
                    t_type = SellTransaction()
                else:
                    t_type = BuyTransaction()
                tran_item = Transaction(x[0], time_in_datetime, t_type, x[4], x[3])
                tran_item.tran_id = x[1]
                output.append(tran_item)

            return output
        except Error:
            print(Error)
        finally:
            conn.close()


