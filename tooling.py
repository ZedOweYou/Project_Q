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
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

#convert from pandas dataframe to kdb table
def pandas_to_kdb(df: DataFrame) -> Table:
    q.set('t',q('!', df.columns, [np.array(df[x]) for x in df.columns]))
    q('t:flip t')
    t = q("select from t") 
    return t

#convert python utc datetime to est datetime
def utc_to_est(dt: datetime) -> datetime:
    est_tz = ZoneInfo("America/New_York")
    dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(est_tz)