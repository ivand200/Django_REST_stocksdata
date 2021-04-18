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

    SP500.objects.all().delete()

    with open('SP500_components_raw.json', 'r') as f:
        file = f.read()
    data = json.loads(file)
    for item in data:
        symbol_ = item["Symbol"]
        name_ = item["Name"]
        mom_12_2 = fun.get_mom_12_1(item["Symbol"])
        pe = fun.get_pe(item["Symbol"])
        ep = fun.get_ep(item["Symbol"])
        #pdiv = fun.get_div(item["Symbol"])

        s = SP500(symbol=symbol_, name=name_, momentum_12_2=mom_12_2, p_e=pe, e_p=ep)
        s.save()
