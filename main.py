import datetime
import yfinance as yf
from ibapi import wrapper
from ibapi.client import EClient
from ibapi.common import SetOfFloat, SetOfString, TickerId
from ibapi.ticktype import TickType
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time
import requests
import json
import pandas as pd

results = pd.DataFrame()
print("hier")

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def historicalData(self, reqId, bar):
        time.sleep(2)
        print("HistoricalData. ReqId:", reqId, "BarData. ", bar)

    def tickPrice(self, reqId, tickType, price, attrib):
        print('The current ask price is: ', price)

    def securityDefinitionOptionParameter(self, reqId: int, exchange: str, underlyingConId: int, tradingClass: str, multiplier: str, expirations: SetOfString, strikes: SetOfFloat):
        print("here")
        for expiration in expirations:
            for strike in strikes:
                temp = Contract()
                temp.symbol = tradingClass
                temp.secType = "OPT"
                temp.exchange = "SMART"
                temp.currency = "USD"
                temp.lastTradeDateOrContractMonth = expiration
                temp.strike = strike
                temp.right = "C"
                temp.multiplier = "100"
                print(f"Expiration: {expiration}, Strike: {strike}, Exchange: {exchange}, Company: {tradingClass}")
                time.sleep(0.2)
                app.reqHistoricalData(5, temp, queryTime, "2 D", "4 hours", "TRADES", 1, 1, False, [])

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        super().accountSummary(reqId, account, tag, value, currency)
        print("AccountSummary. ReqId:", reqId, "Account:", account, "Tag: ", tag, "Value:", value, "Currency:",
              currency)


def run_loop():
    app.run()


app = IBapi()
app.connect('127.0.0.1', 7496, 123)
api_thread = threading.Thread(target=app.run, daemon=True)
api_thread.start()
time.sleep(10)

print("haha")

contract = Contract()
contract.symbol = "MSFT"
contract.secType = "OPT"
contract.exchange = "SMART"
contract.currency = "USD"
contract.lastTradeDateOrContractMonth = "20230113"
contract.strike = 235
contract.right = "C"
contract.multiplier = "100"

queryTime = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y%m%d-%H:%M:%S")
app.reqHistoricalData(5, contract, queryTime, "2 D", "4 hours", "TRADES", 1, 1, False, [])
app.reqSecDefOptParams(0, "IBM", "", "STK", 8314)
print("hereee")
time.sleep(100)
print("now proceeding")


# Create a list of the top 100 stocks in the US
top_100_stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB', 'JPM', 'XOM', 'V', 'BAC', 'WFC',
                  'T', 'CSCO', 'INTC', 'PFE', 'MCD', 'CVX', 'DIS', 'IBM', 'C', 'VZ',
                  'UNH', 'WMT', 'KO', 'GE', 'NKE', 'BKNG', 'MORGAN STANLEY', 'PEP', 'HON',
                  'ORCL', 'CAT', 'GS', 'MMM', 'CVS', 'HD', 'JNJ', 'UTX', 'WBA', 'MA',
                  'DOW', 'NEE', 'DUK', 'JCI', 'BA', 'HAL', 'CME', 'VMW', 'EXXON MOBIL',
                  'EBAY', 'D', 'AMGN', 'GILD', 'COST', 'HP', 'EPD', 'UNP', 'F', 'CCI',
                  'KMI', 'NOC', 'CMCSA', 'POWR', 'O', 'BP', 'AEP', 'APA', 'COP', 'TMO',
                  'CAG', 'MPC', 'EMR', 'ED', 'FRC', 'PPG', 'CHD', 'CB', 'QCOM', 'CHK',
                  'BAX', 'DOW CHEMICAL', 'LOW', 'HPQ', 'DAL', 'HUM', 'MDLZ', 'BAH', 'AGN',
                  'MDT', 'APC', 'CNI', 'LUV', 'GIS', 'VIAB', 'HP', 'XRX', 'CL']
stock_data = {}
x = 1
for stock in top_100_stocks:
    stock_info = yf.Ticker(stock).info
    closing_price = stock_info['regularMarketPrice']
    dividend_yield = stock_info['dividendYield']
    stock_data[stock] = {'closing_price': closing_price, 'dividend_yield': dividend_yield}
    time.sleep(1)

print(stock_data)
print("end)")




app.disconnect()

#app.reqMktData(1, contract, '', False, False, [])
