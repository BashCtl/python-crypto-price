import sqlite3

conn = sqlite3.connect("./db/coinmarket.sqlite")
cursor = conn.cursor()


class DbReader:

    def __init__(self):
        self.table_data = []

    def get_table_data(self, limit=8):
        statement = f"SELECT * FROM coins ORDER BY id DESC LIMIT {limit}"
        try:
            for row in cursor.execute(statement):
                self.table_data.append(list(row))
            return self.table_data
        except sqlite3.OperationalError as err:
            print(f"Something went wrong: {err}")
        finally:
            conn.close()


if __name__ == "__main__":
    dbreader = DbReader()
    table = dbreader.get_table_data()
    print(table)