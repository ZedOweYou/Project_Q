# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:50:31 2024

@author: ZedOweYou
"""

#tooling.py

import pykx as kx
from pykx import q
import pandas as pd
import numpy as np

def pandas_to_kdb(df):
    q.set('t',q('!', df.columns, [np.array(df[x]) for x in df.columns]))
    q('t:flip t')
    t = q("select from t") 
    return t