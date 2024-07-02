# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:51:58 2024

@author: ZedOweYou
"""

#data_collection.py

#external
import requests
import pykx as kx
from pykx import q
import yfinance as yf
import pandas as pd
import numpy as np

#internal
from tooling import pandas_to_kdb

def get_sym_data(symbols):
    sym = yf.Ticker(symbols)
    df = yf.download(symbols, period="1d",interval="1m",actions=False).reset_index()
    print(df.head())
    t = pandas_to_kdb(df)
    return t


