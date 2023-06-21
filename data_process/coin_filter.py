class DataFilter:

    def __init__(self, data):
        self.data = data["data"]

    def by_symbols(self, *symbols):
        result = []
        for item in self.data:
            if item["symbol"] in symbols:
                result.append(item)
            if len(result) == len(symbols):
                print("=== FILTERED ALL COINS ===")
                break
        return result
