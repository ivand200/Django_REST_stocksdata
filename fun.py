from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table
import yahoo_fin.stock_info as si
import sqlite3
import csv
from datetime import datetime, timedelta
import yfinance as yf
import numpy as np
import pandas as pd
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request, urllib.parse, urllib.error

# Define previous month
now = datetime.now()
lastmonth = now - timedelta(weeks=6)
endoflastmonth = lastmonth.replace(day=28)
month_ago = endoflastmonth.strftime("%Y-%m-%d")

# Shares outstanding
def shares_outstanding(ticker):
    url = (f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=defaultKeyStatistics")
    fhand = urllib.request.urlopen(url).read()
    data = json.loads(fhand)
    shares = (data["quoteSummary"]["result"][0]["defaultKeyStatistics"]["sharesOutstanding"]["raw"])
    return shares

# Average income for last 4 years
def average_income(ticker):
    url = (f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=incomeStatementHistory")
    fhand = urllib.request.urlopen(url).read()
    data = json.loads(fhand)
    year1 = (data["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][0]["netIncome"]["raw"])
    year2 = (data["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][1]["netIncome"]["raw"])
    year3 = (data["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][2]["netIncome"]["raw"])
    year4 = (data["quoteSummary"]["result"][0]["incomeStatementHistory"]["incomeStatementHistory"][3]["netIncome"]["raw"])
    return (year1 + year2 + year3 + year4) / 4


# Last close price
def get_close_price(share):
    try:
        ticker = si.get_quote_table(share)['Previous Close']
        return ticker
    except:
        return 0

# E/P
def get_ep(share):
    try:
        e_p = round(((average_income(share) / shares_outstanding(share)) / get_close_price(share)), 2)
        return e_p
    except:
        return 0

# P/E
def get_pe(share):
    try:
        ticker = si.get_quote_table(share)['PE Ratio (TTM)']
        if ticker == '' or pd.isnull(ticker):
            ticker = 0
        return ticker
    except:
        return 0

# Momentum for last 12 month
def get_mom(share):
    ticker = yf.Ticker(share)
    ticker = ticker.history(start="2000-01-01", end=month_ago, interval="1mo")
    ticker = ticker[ticker["Close"].notna()]
    ticker["Price0"] = ticker["Close"].shift(12)
    ticker["Price1"] = ticker["Close"]
    ticker["mom_12"] = (ticker["Price1"] / ticker["Price0"]) - 1
    return round(ticker["mom_12"][-1], 2)


# last close price compare to MA10, 1 = close higher than MA10
def get_ma(share):
    ticker = yf.Ticker(share)
    ticker = ticker.history(start="2007-01-30", end=month_ago, interval="1mo")
    ticker = ticker[ticker["Close"].notna()]
    ticker["MA10"] = ticker["Close"].rolling(10).mean()
    ticker["Difference"] = (ticker["Close"] / ticker["MA10"]) - 1
    ticker["Direction"] = [1 if ticker.loc[ei, "Difference"] > 0 else -1 for ei in ticker.index]
    result = ticker["Direction"][-1]
    return result

# Momentum_12_2
def get_mom_12_1(share):
    try:
        ticker = si.get_data(f"{share}", start_date = '01/01/2017', end_date = month_ago, interval = '1mo')
        ticker = ticker[ticker["close"].notna()]
        ticker["Price0"] = ticker["close"].shift(12)
        ticker["Price1"] = ticker["close"].shift(1)
        ticker["mom_12_1"] = (ticker["Price1"] / ticker["Price0"]) - 1
        return (round(ticker["mom_12_1"][-1], 2))
    except:
        return 0

# Dividend average for last 5 years / last close price
def get_div(share):
    try:
        div = si.get_dividends(share)[-20:].mean()
        div_income = (div * 4) / get_close_price(share)
        if  len(div_income) < 1:
            div_income = 0
        return round(div_income, 3)
    except:
        return 0
