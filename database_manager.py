# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 08:30:52 2024

@author: ZedOweYou
"""

#database_manager.py
#read and writes q tables to splayed table files

#external
from pykx import q
from pykx.wrappers import Table
from pykx.wrappers import SymbolAtom

#internal
from tooling import utc_to_est

def save_table(t: Table, sym: str) -> SymbolAtom:
    p = ('`:data/'+sym+'/ set t')
    return p

def read_table(sym: str) -> Table:
    q('t: get `:data/'+sym+'/')
    return q('select from t')

def latest_date(sym: str) -> datetime:
    q('t: get `:data/'+sym+'/')
    q('t: select from t')
    latest_date = q("max t`Datetime").py()
    return utc_to_est(latest_date)
    