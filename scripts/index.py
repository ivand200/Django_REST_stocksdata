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

    Index.objects.all().delete()

    indxs = {"SP500": "SPY", "DJ30": "^DJI"}

    for key,val in indxs.items():
        symbol_ = val
        name_ = key
        mom = fun.get_mom(val)
        ma = fun.get_ma(val)

        i = Index(symbol=symbol_, name=name_, momentum=mom, ma10=ma)
        i.save()
