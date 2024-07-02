# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:51:58 2024

@author: ZedOweYou
"""

#data_collection.py

#external
from datetime import datetime
from pykx.wrappers import Table
from pykx import q
import yfinance as yf

#internal
from tooling import pandas_to_kdb
import database_manager as dm

#pull data from yfinance convert to kdb table
def get_sym_data(symbol:str, start: datetime=None) -> Table:
    sym = yf.Ticker(symbol)
    if start!=None:
        df = sym.history(start=start,interval="1m",actions=False).reset_index()
    else:
        df = sym.history(period="1d",interval="1m",actions=False).reset_index()
    t = pandas_to_kdb(df)
    return t

#get latest date from table, only pull data from after that date
def update_sym_data(symbol:str) -> Table:
    t = dm.read_table(symbol)
    print(q("t"))
    return t






