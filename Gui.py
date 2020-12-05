from tkinter import messagebox
from tkinter import *
import tkinter
import constants


class Gui:

    def __init__(self):
        self.__stocklist_object = None
        self.__portfolio_value_object = None
        self.__dow_ticker_value_object = None
        self.__nasdaq_ticker_value_object = None
        self.__nyse_ticker_value_object = None
        self.__status_object = None

    def generate_info_popup(self, header, message):
        messagebox.showinfo(header, message)

    def generate_error_popup(self, header, message):
        messagebox.showerror(header, message)

    def main_window(self):
        top_level_window = tkinter.Tk()
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

        stock_menu.add_command(label="Add Stock", command=self.dummy_command)
        stock_menu.add_command(label="Delete Stock", command=self.dummy_command)

        tran_menu.add_command(label='Add Transaction', command=self.dummy_command)
        tran_menu.add_command(label='Delete Transaction', command=self.dummy_command)

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

        stock_refresh_button = Button(middle_frame, width=15, text='Refresh Stock List')
        stock_refresh_button.grid(row=0, column=1)

        ticker_refresh_button = Button(middle_frame, width=15, text='Refresh Ticker')
        ticker_refresh_button.grid(row=0, column=0)

        stock_label = Label(label_frame, bd=2, text='STOCK               PRICE               DATE OF LAST PRICE               QUANITY               STOCK TOTAL')
        stock_label.grid_propagate(0)
        stock_label.grid(row=0)

        top_level_window.mainloop()

    def adjust_status(self, message):
        self.__status_object.config(text=message)

    def adjust_stock_list(self, list_of_stocks):
        if not isinstance(list_of_stocks, list):
            raise ValueError("Wrong input type")
        for x in list_of_stocks:
            self.__stocklist_object.insert(END, x)

    def clear_stock_list(self):
        self.__stocklist_object.delete(0, END)

    def dummy_command(self):
        print("dummy_command_execute")

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

    
if __name__ == '__main__':
    test = Gui()
    test.main_window()

