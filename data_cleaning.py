# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:35:11 2024.

@author: ZedOweYou
"""

# data_cleaning.py
from pykx import q
from pykx.wrappers import Table


def foward_fill(t: Table) -> Table:
    """
    Forward fills missing values in the input table `t`.

    Parameters.
        t (Table): Input table containing data with missing values.

    Returns.
        Table: Table with missing values forward filled.
    """
    q.set('t', t)
    return q('fills t')


def process_returns(t: Table) -> Table:
    """
    Process table prices.

    Normalize the input table `t` by (price-price1)*100/price1 to new columns
    Get normalized column deltas as interval returns
    Get interval returns cumulative sums as cumulative returns

    Parameters.
        t (Table): Input table to be normalized.

    Returns.
        Table: Normalized table.
    """
    q('f: `:./data_cleaning.q')
    q('if[f~key f; system "l ", string f]')
    return q('normTable', t)
