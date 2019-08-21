# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:19:03 2019

@author: 72669
"""

import camelot as cl
tables = cl.read_pdf("9-1effective.pdf",flavor = 'stream',pages = 'all')

import pandas as pd
dfs = pd.DataFrame()
for table in tables:
    dfs = pd.concat([dfs,table.df.iloc[4:]])
    
    
dfs.to_excel("9-1effective.xlsx",index = False)