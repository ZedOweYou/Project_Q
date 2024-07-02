# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 08:30:52 2024

@author: ZedOweYou
"""

# database_manager.py
# read and writes q tables to splayed table files

# external
from datetime import datetime

from pykx import q
from pykx.wrappers import Table
from pykx.wrappers import SymbolAtom


# internal
from tooling import utc_to_est


def save_table(t: Table, sym: str) -> SymbolAtom:
    """
    Save a kdb+ Table `t` to a specified symbol directory.

    Args.
        t (Table): The kdb+ Table to be saved.
        sym (str): The symbol representing the file or directory name.

    Returns.
        SymbolAtom: The symbol representing the saved file path or identifier.
    """
    q.set('t', t)
    return q('`:data/'+sym+'/ set t')


def read_table(sym: str) -> Table:
    """
    Read a kdb+ Table stored under the symbol `sym` in the 'data' directory.

    Args.
        sym (str): The symbol representing the file or directory name.

    Returns.
        Table: The kdb+ Table read from the specified location.
    """
    q('t: get `:data/'+sym+'/')
    return q('select from t')


def latest_date(sym: str) -> datetime:
    """
    Retrieve the latest datetime from a kdb+ Table for given symbol.

    Args.
        sym (str): The symbol representing the file or directory name.

    Returns.
        datetime: The latest datetime converted from UTC to Eastern (EST/EDT).
    """
    q('t: get `:data/'+sym+'/')
    q('t: select from t')
    latest_date_value = q("max t`Datetime").py()
    return utc_to_est(latest_date_value)
