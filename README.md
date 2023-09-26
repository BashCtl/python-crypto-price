# Application to send crypto currencies price to mail

## Description:
    Simplte example of using Python and OOP
 Application stores price to db and sends price of the specified currencies  "BTC", "ETH", "XRP", "ADA", "DOGE", "SOL", "DOT", "SHIB",
 to mail address in form of html table. For getting price using API from https://pro.coinmarketcap.com/
 API documents: https://coinmarketcap.com/api/documentation/v1/

### Installation locally:
 * Install Python 3
 * create .env file in the root of project
 * Specify next environment variables in file:
    - API_KEY= can be requested from https://pro.coinmarketcap.com/ (Basix plan no cost needed)
    - APP_PASS= cam be generated in your gmail account, how to do can be found here https://support.google.com/accounts/answer/185833?hl=en
    - LOGIN_MAIL= email account in which was generated APP_PASS
    - SEND_MAIL= email account where to send table of the currencies price
 * Install requirements:
    - pip install -r requirements.txt

### Run program from the root directory:
   - python start.py
### Result table
![Alt text](./result_table.png?raw=true "Currencies table")