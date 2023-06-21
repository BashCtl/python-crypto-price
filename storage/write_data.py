import json
import time
from pathlib import Path


class WriteData:

    def __init__(self, data):
        self.data = data

    def write_json(self):
        file_path = Path().resolve()
        file_name = f"{file_path}/storage/collected_data/coin_info{time.time()}.json"
        with open(file_name, mode="w") as json_file:
            json.dump(self.data, json_file)
