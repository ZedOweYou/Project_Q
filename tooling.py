# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:50:31 2024

@author: ZedOweYou
"""

#tooling.py

from pykx.wrappers import Table
from pykx import q
from pandas.core.frame import DataFrame
import numpy as np

#convert from pandas dataframe to kdb table
def pandas_to_kdb(df: DataFrame) -> Table:
    q.set('t',q('!', df.columns, [np.array(df[x]) for x in df.columns]))
    q('t:flip t')
    t = q("select from t") 
    return t