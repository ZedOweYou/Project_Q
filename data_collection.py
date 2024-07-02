# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:51:58 2024

@author: ZedOweYou
"""

#data_collection.py

#external
from datetime import datetime
from pykx.wrappers import Table
import yfinance as yf

#internal
from tooling import pandas_to_kdb
import database_manager as dm
import error_manager as em

#pull data from yfinance convert to kdb table
def get_sym_data(symbol:str, start: datetime=None, pandas: bool=False)-> Table:
    sym = yf.Ticker(symbol)
    if start!=None:
        df = sym.history(start=start,interval="1m",actions=False).reset_index()
    else:
        df = sym.history(period="1d",interval="1m",actions=False).reset_index()
    if len(df)==0: 
        raise em.NoData("No Data Recieved from yfinance")
    if pandas:
        return df 
    t = pandas_to_kdb(df)
    return t

#get latest datetime from table, only pull data from sym after that date
def get_new_sym_data(symbol:str) -> Table:
    latest_date = dm.latest_date(symbol)
    t = get_sym_data(symbol,start=latest_date)
    return t






