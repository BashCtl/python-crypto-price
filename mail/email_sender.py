import smtplib
import os
from email.message import EmailMessage
from string import Template
from storage.db_reader import DbReader
from data_process.generate_table import HtmlTable
from pathlib import Path
from dotenv import load_dotenv


class EmailSender:

    def __init__(self, htmltable):
        load_dotenv()
        self.htmltable = htmltable
        self.email = EmailMessage()
        self.login_email = os.getenv("LOGIN_MAIL")
        self.app_pass = os.getenv("APP_PASS")

    def set_email(self, destination):

        html = Template(Path("./mail/index.html").resolve().read_text())
        self.email["from"] = "Coin Collector"
        self.email["to"] = destination
        self.email["subject"] = "Crypto Price"
        self.email.set_content(html.substitute(table=self.htmltable), "html")
        return self

    def send_email(self):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.login_email, self.app_pass)
            smtp.send_message(self.email)
            print("Email was sent.")


if __name__ == "__main__":
    dbreader = DbReader()
    table = dbreader.get_table_data()
    htmlgen = HtmlTable(table)
    html_table = htmlgen.get_table()
    print(html_table)
    email_sender = EmailSender(html_table)
    email_sender.set_email(os.getenv("SEND_MAIL"))
    email_sender.send_email()
