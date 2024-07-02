# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 08:30:52 2024.

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


def append_table(t1: Table, t2: Table) -> Table:
    """
    Append the contents of a kdb+ Table `t2` to a kdb+ Table `t1`.

    Args.
        t1 (Table): The first kdb+ Table.
        t2 (Table): The second kdb+ Table to append to the first.

    Returns.
        Table: A new kdb+ Table containing contents of `t1` and `t2`.
    """
    q.set('t1', t1)
    q.set('t2', t2)
    q('t3: t1 upsert select from t2')
    # remove duplicate entries upon return
    return q('distinct t3')


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


