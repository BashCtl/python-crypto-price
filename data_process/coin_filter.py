class DataFilter:

    def __init__(self, data):
        """

        :param data: cryptocurrencies data
        """
        self.data = data["data"]

    def by_symbols(self, *symbols):
        """

        :param symbols: Cryptocurrencies symbols  to filter overall data by symbol field
        :return: filtered currencies
        """
        result = [item for item in self.data if item["symbol"] in symbols]
        print("=== FILTERED ALL COINS ===")
        return result
