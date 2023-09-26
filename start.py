import os
from api.coin_market import CoinMarket
from data_process.coin_filter import DataFilter
from storage.write_data import WriteData
from storage.db_storage import DbStorage
from storage.db_reader import DbReader
from data_process.generate_table import HtmlTable
from mail.email_sender import EmailSender
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    market = CoinMarket()
    listing = market.get_listing_latest()
    data = DataFilter(listing).by_symbols("BTC", "ETH", "XRP", "ADA", "DOGE", "SOL", "DOT", "SHIB")
    # save data locally in json format
    # writer = WriteData(data)
    # writer.write_json()
    # save data to sqlite db
    db_storage = DbStorage(data)
    db_storage.save_to_db()

    # Read last data from DB
    dbreader = DbReader()
    data = dbreader.get_table_data()
    htmlgen = HtmlTable(data)
    # Generate html table
    html_table = htmlgen.get_table()
    email_sender = EmailSender(html_table)
    email_sender.set_email(os.getenv("SEND_MAIL")).send_email()

