from datetime import datetime
from tkinter import messagebox
from tkinter import *
import tkinter
import constants
from Api import Api
from Stock import Stock
from Transaction import Transaction
from constants import BuyTransaction, SellTransaction
from Database import Database


class Gui:

    def __init__(self):
        self.selected_tran_for_delete = None
        self.tran_output_frame = None
        self.top_window = None
        self.delete_transaction_get_stock_window_radio_selected_stock = None
        self.delete_transaction_get_transaction_window_object = None
        self.delete_transaction_get_stock_window_object = None
        self.enter_transaction_window_date_entry = None
        self.enter_transaction_window_price_entry = None
        self.enter_transaction_window_share_entry = None
        self.enter_transaction_window_object = None
        self.delete_stock_window_object = None
        self.delete_stock_radio_value = None
        self.enter_transaction_stock_radio_value = None
        self.action_for_transaction_stringVar_object = None
        self.__stocklist_object = None
        self.__portfolio_value_object = None
        self.__dow_ticker_value_object = None
        self.__nasdaq_ticker_value_object = None
        self.__nyse_ticker_value_object = None
        self.__status_object = None
        self.__stock_display_total = 0
        self.__stock_entry_entry_object = None
        self.__stock_entry_window_object = None

    def generate_info_popup(self, header, message):
        messagebox.showinfo(header, message)

    def generate_error_popup(self, header, message):
        messagebox.showerror(header, message)

    def main_window(self):
        top_level_window = tkinter.Tk()
        self.top_window = top_level_window
        top_level_window.title(constants.PROGRAM_NAME)
        #top_level_window.grid_propagate(0)

        # menu build
        main_menu = tkinter.Menu()
        top_level_window.config(menu=main_menu)

        stock_menu = Menu(main_menu)
        tran_menu = Menu(main_menu)
        exit_menu = Menu(main_menu)

        main_menu.add_cascade(label='Stock', menu=stock_menu)
        main_menu.add_cascade(label='Transaction', menu=tran_menu)
        main_menu.add_cascade(label='Exit', menu=exit_menu)

        stock_menu.add_command(label="Add Stock", command=self.enter_stock_window)
        stock_menu.add_command(label="Delete Stock", command=self.delete_stock_window)

        tran_menu.add_command(label='Add Transaction', command=self.enter_transaction_window)
        tran_menu.add_command(label='Delete Transaction', command=self.delete_transaction)

        exit_menu.add_command(label='Exit', command=top_level_window.destroy)

        data_frame = Frame(top_level_window, height=500, width=500)
        label_frame = Frame(top_level_window, height=25, width=500)
        middle_frame = Frame(top_level_window, height=50, width=500)
        ticker_frame = Frame(top_level_window, height=50, width=500)
        status_bar = Frame(top_level_window, height=20, width=500)
        data_frame.grid_propagate(0)
        middle_frame.grid_propagate(0)
        ticker_frame.grid_propagate(0)
        status_bar.grid_propagate(0)
        label_frame.grid_propagate(0)

        label_frame.grid(row=0)
        data_frame.grid(row=1)
        middle_frame.grid(row=2)
        ticker_frame.grid(row=3)
        status_bar.grid(row=4)

        # status bar
        status = Label(status_bar, text='Welcome to stock organizer', bd=1, relief=SUNKEN, anchor=W, width=500)
        self.__status_object = status
        status.grid(row=0, sticky=EW)

        dow_ticker = Label(ticker_frame, text='DOW:')
        dow_ticker.grid_propagate(0)
        dow_ticker.grid(row=0, column=0)

        dow_value = Label(ticker_frame, text='dow_value')
        self.__dow_ticker_value_object = dow_value
        dow_value.grid_propagate(0)
        dow_value.grid(row=0, column=1)

        nasdaq_ticker = Label(ticker_frame, text='NASDAQ:')
        nasdaq_ticker.grid_propagate(0)
        nasdaq_ticker.grid(row=0, column=2)

        nasdaq_value = Label(ticker_frame, text='nasdaq_value')
        self.__nasdaq_ticker_value_object = nasdaq_value
        nasdaq_value.grid_propagate(0)
        nasdaq_value.grid(row=0, column=3)

        nyse_ticker = Label(ticker_frame, text = 'NYSE:')
        nyse_ticker.grid_propagate(0)
        nyse_ticker.grid(row=0, column=4)

        nyse_value = Label(ticker_frame, text= 'nyse_value')
        self.__nyse_ticker_value_object = nyse_value
        nyse_value.grid_propagate(0)
        nyse_value.grid(row=0, column=5)

        stock_list = Listbox(data_frame, height=450, width=500)
        self.__stocklist_object = stock_list
        stock_list.grid_propagate(0)
        stock_list.grid(row=1)

        portfolio_total = Label(middle_frame, text='PORTFOLIO TOTAL:')
        portfolio_total.grid_propagate(0)
        portfolio_total.grid(row=0, column=2, sticky=E)

        portfolio_value = Label(middle_frame, text='portfolio_value')
        self.__portfolio_value_object = portfolio_value
        portfolio_value.grid_propagate(0)
        portfolio_value.grid(row=0, column=3, sticky=E)

        stock_refresh_button = Button(middle_frame, width=15, text='Refresh Stock List', command=self.generate_main_stock_window_list)
        stock_refresh_button.grid(row=0, column=1)

        ticker_refresh_button = Button(middle_frame, width=15, text='Refresh Ticker')
        ticker_refresh_button.grid(row=0, column=0)

        stock_label = Label(label_frame, bd=2, text='STOCK                  PRICE               DATE OF LAST PRICE           QUANITY           STOCK TOTAL')
        stock_label.grid_propagate(0)
        stock_label.grid(row=0)
        self.generate_main_stock_window_list()
        top_level_window.mainloop()

    def enter_stock_window(self):
        root_window = tkinter.Tk()
        root_window.title("Add Stock")
        entry_frame = Frame(root_window)
        button_frame = Frame(root_window)
        entry_frame.pack()
        button_frame.pack(side=BOTTOM)
        enter_button = Button(button_frame, text='Enter', command=self.process_stock_entry)
        exit_button = Button(button_frame, text='Cancel', command=root_window.destroy)
        enter_button.pack(side=LEFT)
        exit_button.pack()
        entry_label = Label(entry_frame, text="Enter stock symbol")
        entry_widget = Entry(entry_frame)
        entry_widget.pack(side=RIGHT)
        entry_label.pack(side=LEFT)
        self.__stock_entry_entry_object = entry_widget
        self.__stock_entry_window_object = root_window
        root_window.mainloop()

    def process_stock_entry(self):
        stock_name_to_add = self.__stock_entry_entry_object.get()
        database = Database()
        database.create_new_stock(stock_name_to_add)
        self.__stock_entry_window_object.destroy()
        self.adjust_status("New Stock Added")

    def enter_transaction_window(self):

        database = Database()
        stock_list = database.get_all_stocks()
        root_window = Toplevel()
        root_window.title("Enter New Transaction")
        self.enter_transaction_window_object = root_window
        radio_frame = Frame(root_window)
        radio_frame.grid(row=0)
        entry_frame = Frame(root_window)
        entry_frame.grid(row=1)
        button_frame = Frame(root_window)
        button_frame.grid(row=2)

        enter_button = Button(button_frame, text='Enter', command=self.process_transaction_entry)
        enter_button.grid(row=0, column=0)

        cancel_button = Button(button_frame, text='Cancel', command=root_window.destroy)
        cancel_button.grid(row=0, column=1)

        date_entry_label = Label(entry_frame, text='Enter Date:')
        date_entry = Entry(entry_frame)
        self.enter_transaction_window_date_entry = date_entry
        date_entry_label.grid(row=0, column=0)
        date_entry.grid(row=0, column=1)

        self.action_for_transaction_stringVar_object = StringVar()
        radio_label = Label(entry_frame, text='Select Transaction')
        buy_radio = Radiobutton(entry_frame, text='Buy', value='buy', variable=self.action_for_transaction_stringVar_object)
        sell_radio = Radiobutton(entry_frame, text='Sell', value='sell', variable=self.action_for_transaction_stringVar_object)
        radio_label.grid(row=1, column=0)
        buy_radio.grid(row=1, column=1)
        sell_radio.grid(row=1, column=2)

        share_label = Label(entry_frame, text='Shares:')
        share_entry = Entry(entry_frame)
        self.enter_transaction_window_share_entry = share_entry
        share_label.grid(row=2, column=0)
        share_entry.grid(row=2, column=1)

        price_label = Label(entry_frame, text='Price:')
        price_entry = Entry(entry_frame)
        self.enter_transaction_window_price_entry = price_entry
        price_label.grid(row=3, column=0)
        price_entry.grid(row=3, column=1)

        self.enter_transaction_stock_radio_value = StringVar()
        for x in range(len(stock_list)):
            radio = Radiobutton(radio_frame, text=stock_list[x].symbol, variable=self.enter_transaction_stock_radio_value, value=stock_list[x].symbol)
            radio.grid(row=x)

        root_window.mainloop()


    def process_transaction_entry(self):

        action_object = None
        stock_name = self.enter_transaction_stock_radio_value.get()
        price = self.enter_transaction_window_price_entry.get()
        stock_quanity = self.enter_transaction_window_share_entry.get()
        date_to_save = datetime.strptime(self.enter_transaction_window_date_entry.get(), "%m-%d-%Y")

        if self.action_for_transaction_stringVar_object.get() == 'buy':
            action_object = BuyTransaction()
        else:
            action_object = SellTransaction()

        transactions_to_save = Transaction(stock_name, date_to_save, action_object, price, stock_quanity)
        database = Database()
        database.save_transaction(transactions_to_save)
        self.enter_transaction_window_object.destroy()
        self.adjust_status("New Transaction Added")

    def delete_stock_window(self):

        database = Database()
        stockList = database.get_all_stocks()
        root = Toplevel()
        root.title("Delete Stock")
        self.delete_stock_window_object = root
        selection_frame = Frame(root)
        button_frame = Frame(root)

        selection_frame.grid(row=0)
        button_frame.grid(row=1)

        exit_button = Button(button_frame, text='Exit', command=root.destroy)
        enter_button = Button(button_frame, text='Enter', command=self.process_delete_stock)
        exit_button.grid(row=0, column=1)
        enter_button.grid(row=0, column=0)

        self.delete_stock_radio_value = StringVar()
        for x in range(len(stockList)):
            radio = Radiobutton(selection_frame, text=stockList[x].symbol, variable=self.delete_stock_radio_value,
                                value=stockList[x].symbol)
            radio.grid(row=x)
        root.mainloop()

    def process_delete_stock(self):
        database = Database()
        stock_to_delete = database.get_stock(self.delete_stock_radio_value.get())
        database.delete_stock(stock_to_delete)
        self.delete_stock_window_object.destroy()
        self.adjust_status("Stock and associated transactions have been deleted")

    def delete_transaction(self):
        database = Database()
        stockList = database.get_all_stocks()

        root_window = Toplevel(self.top_window)
        root_window.title("Delete Transaction")
        self.delete_transaction_get_stock_window_object = root_window
        selection_frame = Frame(root_window)
        tran_output_frame = Frame(root_window)
        self.tran_output_frame = tran_output_frame
        button_frame = Frame(root_window)

        selection_frame.grid(row=0)
        button_frame.grid(row=2)
        tran_output_frame.grid(row=1)

        exit_button = Button(button_frame, text='Exit', command=root_window.destroy)
        enter_button = Button(button_frame, text='Enter', command=self.process_delete_transaction)
        get_tran_button = Button(button_frame, text='Get Transactions', command=self.add_delete_transactions_items)
        exit_button.grid(row=0, column=1)
        enter_button.grid(row=0, column=0)
        get_tran_button.grid(row=0, column=2)

        self.delete_transaction_get_stock_window_radio_selected_stock = StringVar()

        for x in range(len(stockList)):
            radio = Radiobutton(selection_frame, text=stockList[x].symbol,
                                variable=self.delete_transaction_get_stock_window_radio_selected_stock,
                                value=stockList[x].symbol)
            radio.grid(row=x)

        root_window.mainloop()

    def add_delete_transactions_items(self):
        database = Database()
        tran_list = database.get_transactions(self.delete_transaction_get_stock_window_radio_selected_stock.get())

        self.selected_tran_for_delete = StringVar()

        label = Label(self.tran_output_frame, text='           Stock Transaction Price Shares')
        label.grid(row=0)

        for x in range(len(tran_list)):
             radio = Radiobutton(self.tran_output_frame, text=tran_list[x].symbol + "    " + tran_list[x].action.tran_type()
                                                          + "      " + str(tran_list[x].price) + "        " + str(
             tran_list[x].number_of_shares)
                           , variable=self.selected_tran_for_delete,
                          value=tran_list[x].tran_id)
             radio.grid(row=x+1)


    def process_delete_transaction(self):
        database = Database()
        database.delete_individual_transaction_using_primary_key(self.selected_tran_for_delete.get())
        self.delete_transaction_get_stock_window_object.destroy()
        self.adjust_status("Transaction deleted")


    def adjust_status(self, message):
        self.__status_object.config(text=message)



    def adjust_stock_list(self, list_of_stocks):
        self.__stock_display_total = 0
        self.clear_stock_list()
        insert_string = ""
        if not isinstance(list_of_stocks, list):
            raise ValueError("Wrong input type")
        if len(list_of_stocks) == 0:
            self.__stocklist_object.insert(END, "No stocks saved")
        else:
            for x in list_of_stocks:
                insert_string += x.symbol
                insert_string += constants.STOCK_WINDOW_SPACE_BETWEEN_FIELDS
                insert_string += str(x.last_price)
                insert_string += constants.STOCK_WINDOW_SPACE_BETWEEN_FIELDS
                insert_string += str(x.last_price_update)
                insert_string += constants.STOCK_WINDOW_SPACE_BETWEEN_FIELDS
                insert_string += str(x.calculate_current_shares())
                insert_string += constants.STOCK_WINDOW_SPACE_BETWEEN_FIELDS
                insert_string += str(x.calculate_current_shares()*x.last_price)
                self.__stock_display_total += x.calculate_current_shares() * x.last_price
                self.__stocklist_object.insert(END, insert_string)
                insert_string = ""
        # TODO put total calculations in own method
        self.adjust_portfolio_value(str(self.__stock_display_total))

    def clear_stock_list(self):
        self.__stocklist_object.delete(0, END)

    def adjust_nyse_value(self, text):
        if not isinstance(text, str):
            raise ValueError("Invalid input, use string")
        self.__nyse_ticker_value_object.config(text=text)

    def adjust_nasdaq_value(self, text):
        if not isinstance(text, str):
            raise ValueError("invalid input, use string")
        self.__nasdaq_ticker_value_object.config(text=text)

    def adjust_dow_value(self, text):
        if not isinstance(text, str):
            raise ValueError("Invalid input, use string")
        self.__dow_ticker_value_object.config(text=text)

    def adjust_portfolio_value(self, text):
        if not isinstance(text, str):
            raise ValueError("Invalid input, use string")
        self.__portfolio_value_object.config(text=text)

    def generate_main_stock_window_list(self):
        database = Database()
        complete_list_of_stocks = []
        list_of_bare_stocks = database.get_all_stocks()
        ready_for_display_stocks = []

        for x in list_of_bare_stocks:
             item = database.get_stock(x.symbol)
             complete_list_of_stocks.append(item)

        api = Api()

        for z in complete_list_of_stocks:
            item = api.get_stock_quote(z)
            ready_for_display_stocks.append(item)

        self.adjust_stock_list(ready_for_display_stocks)

if __name__ == '__main__':
    test = Gui()

    test.main_window()
