# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:28:03 2024.

@author: zedoweyou
"""

# setup.py
# just testing kx licensing and environment

import pykx as kx
from pykx import q

# Print a welcome message from q
q("system \"echo 'Hello, Q!'\"")

# create a table with a large set of random numbers
q("col1: 1000000?100")
q("col2: 1000000?120")
q("t:([]col1:col1;col2:col2)")
# Fetch the table back into Python
table = q("5# select col1,col2 from t")
# Print the table
print(table)

# testing lists
py_list = [1, 2, 3, 4, 5]
q.set('list_test', kx.toq(py_list))
print(q("list_test"))
