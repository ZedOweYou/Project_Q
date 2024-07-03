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


def tablesomething(t: Table) -> Table:
    """
    Normalize the input table `t` using a predefined normalization method.

    Parameters.
        t (Table): Input table to be normalized.

    Returns.
        Table: Normalized table.
    """
    q('\l data_cleaning.q')
    return q('normTable', t)
