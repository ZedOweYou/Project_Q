# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:51:58 2024

@author: ZedOweYou
"""

# data_collection.py

# external
from typing import Union

from datetime import datetime
from pykx.wrappers import Table
import yfinance as yf
from pandas import DataFrame

# internal
from tooling import pandas_to_kdb
import database_manager as dm
import error_manager as em


def get_sym_data(symbol: str,
                 start: datetime = None,
                 pandas: bool = False) -> Union[Table, DataFrame]:
    """
    Retrieve historical stock data from Yahoo Finance.

    Parameters.
    symbol (str): The stock symbol to retrieve data for.

    start (datetime, optional): The start date for the historical data.

    If None, defaults to the past 1 day.
    pandas (bool, optional): If True, return the data as a pandas DataFrame.
    If False, convert to a kdb+ table.

    Returns.
    Table or DataFrame: The historical stock data as a kdb+ table
    or pandas DataFrame.

    Raises.
    NoData: If no data is received from Yahoo Finance.
    """
    sym = yf.Ticker(symbol)
    if start is not None:
        df = sym.history(start=start, interval="1m", actions=False)
        df = df.reset_index()
    else:
        df = sym.history(period="1d", interval="1m", actions=False)
        df = df.reset_index()
    if len(df) == 0:
        raise em.NoData("No Data Recieved from yfinance")
    if pandas:
        return df
    t = pandas_to_kdb(df)
    return t


def get_new_sym_data(symbol: str) -> Table:
    """
    Retrieve new stock data for a given symbol from Yahoo Finance.

    Parameters.
    symbol (str): The stock symbol to retrieve data for.

    Returns.
    Table: The historical stock data as a kdb+ table.

    Raises.
    NoData: If no data is received from Yahoo Finance.
    """
    latest_date = dm.latest_date(symbol)
    t = get_sym_data(symbol, start=latest_date)
    return t
