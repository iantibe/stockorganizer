import requests
import json
import constants
from Stock import Stock
from datetime import datetime

class Api:
    def __init__(self):
        pass

    def get_stock_quote(self, stock):
        if not isinstance(stock, Stock):
            raise ValueError("Invalid input. Please use a Stock object")
        response = requests.get(constants.generate_url(stock.symbol))
        json_object_quote = json.loads(response.content)
        if json_object_quote == constants.API_ERROR_MESSAGE:
            raise ValueError("Invalid api call")
        data_set = json_object_quote["Time Series (1min)"]
        x = data_set.items()
        key = list(data_set)[0]
        quote_date = datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
        quotes = data_set.get(key)
        stock.last_price = float(quotes.get("2. high"))
        stock.last_price_update = quote_date
        return stock
