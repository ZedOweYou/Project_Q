# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:50:31 2024

@author: ZedOweYou
"""

# tooling.py
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from pykx.wrappers import Table
from pykx import q
from pandas.core.frame import DataFrame
import numpy as np



def pandas_to_kdb(df: DataFrame) -> Table:
    """
    Convert a pandas DataFrame to a kdb+ Table.

    Args.
        df (DataFrame): The pandas DataFrame to be converted.

    Returns.
        Table: A kdb+ Table containing the data from the DataFrame.

    Raises.
        AssertionError: If the input `df` is not a pandas DataFrame.
        ValueError: If conversion fails due to incompatible data types.
    """
    q.set('t', q('!', df.columns, [np.array(df[x]) for x in df.columns]))
    q('t:flip t')
    t = q("select from t")
    return t


def utc_to_est(dt: datetime) -> datetime:
    """
    Convert a UTC datetime object to Eastern Standard Time (EST).

    Args.
        dt (datetime): The UTC datetime object to be converted.

    Returns.
        datetime: A datetime object representing the equivalent time in EST.
    """
    est_tz = ZoneInfo("America/New_York")
    dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(est_tz)
