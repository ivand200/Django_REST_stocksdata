from stocks_rest.models import SP500, DJ30, Div, Index

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
import fun

def run():
    Div.objects.all().delete()

    with open('dividend_aristocrats.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol_ = row[1]
            name_ = row[0]
            div_p = fun.get_div(row[1])

            d = Div(symbol=symbol_, name=name_, p_div=div_p)
            d.save()
