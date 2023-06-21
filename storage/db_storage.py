import sqlite3

conn = sqlite3.connect("./db/coinmarket.sqlite")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS coins (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT  NOT NULL,"
               " symbol TEXT NOT NULL,"
               "price BLOB NOT NULL, last_update TIMESTAMP NOT NULL)")


class DbStorage:

    def __init__(self, filtered_data):
        self.filtered_data = filtered_data

    def save_to_db(self):
        try:
            for coin in self.filtered_data:
                name = coin["name"]
                symbol = coin["symbol"]
                price = coin["quote"]["USD"]["price"]
                last_update = coin["last_updated"]
                cursor.execute("INSERT INTO coins(name, symbol, price, last_update) VALUES(?, ?, ?, ?)",
                               (name, symbol, price, last_update))
                conn.commit()
                print(f"{name} saved to DB.")
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
            print(f"Failed to save to DB: {err}")
        finally:
            conn.close()
