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

    DJ30.objects.all().delete()

    with open('DJ30.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol_ = row[1]
            name_ = row[0]
            mom_12_2 = fun.get_mom_12_1(row[1])
            pe = fun.get_pe(row[1])
            ep = fun.get_ep(row[1])
            pdiv = fun.get_div(row[1])

            d = DJ30(symbol=symbol_, name=name_, momentum_12_2=mom_12_2, p_e=pe, e_p=ep, p_div=pdiv)
            d.save()
