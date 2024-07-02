# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:51:58 2024

@author: ZedOweYou
"""

#data_collection.py

#external
from pykx.wrappers import Table
import yfinance as yf

#internal
from tooling import pandas_to_kdb

#pull data from yfinance convert to kdb table
def get_sym_data(symbol:str) -> Table:
    sym = yf.Ticker(symbol)
    df = sym.history(period="1d",interval="1m",actions=False).reset_index()
    print(df.head())
    t = pandas_to_kdb(df)
    return t





