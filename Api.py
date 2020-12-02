import requests
import json
import constants


class Api:
    def __init__(self):
        pass

    def get_stock_quote(self, sym):
        response = requests.get(constants.generate_url(sym))
        json_object_quote = json.loads(response.content)
        if json_object_quote["Error Message"] == constants.API_ERROR_MESSAGE:
            raise ValueError("Invalid api call")
        data_set = json_object_quote["Time Series (1min)"]
        x = data_set.items()
        key = list(data_set)[0]
        quotes = data_set.get(key)
        return float(quotes.get("2. high"))
