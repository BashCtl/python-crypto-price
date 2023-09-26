import json
import os
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv


class CoinMarket:

    def __init__(self):

        load_dotenv()
        # specifying default values for api request
        self.start = "1"
        self.limit = "1000"
        self.currency = "USD"
        self.sort = "market_cap"
        self.base_url = "https://pro-api.coinmarketcap.com"
        self.session = Session()
        self.session.headers.update(CoinMarket.headers())

    def set_start(self, start):
        self.start = start
        return self

    def set_limit(self, limit):
        self.limit = limit
        return self

    def set_convert_to(self, currency):
        self.currency = currency
        return self

    def set_sort_by(self, sort):
        self.sort = sort
        return self

    def set_params(self, start, limit, sort, convert):
        self.start = start
        self.limit = limit
        self.sort = sort
        self.convert = convert
        return self

    def params(self):
        return {
            "start": self.start,
            "limit": self.limit,
            "sort": self.sort,
            "convert": self.currency
        }

    @staticmethod
    def headers():
        return {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": os.getenv("API_KEY")
        }

    def get_listing_latest(self):
        endpoint = "/v1/cryptocurrency/listings/latest"
        try:
            response = self.session.get(f"{self.base_url}{endpoint}", params=self.params())
            return json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as err:
            print(err)

# if __name__ == "__main__":
#     market = CoinMarket()
#     listing = market.get_listing_latest()
#     coin_filter = DataFilter(listing)
#     data = coin_filter.by_symbols("BTC", "ETH", "XRP", "ADA", "DOGE", "SOL", "DOT", "SHIB")
#     writer = WriteData(data)
#     writer.write_json()
#     db_storage = DbStorage(data)
#     db_storage.save_to_db()
