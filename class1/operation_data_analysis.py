# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:47:47 2019

@author: 72669
"""

import pandas as pd
platform1 = pd.read_excel("平台投放数据.xlsx",sheet_name = '平台一')[['日期','渠道','实际消耗','展示数','点击数','点击率']]
platform2 = pd.read_excel("平台投放数据.xlsx",sheet_name = '平台二')[['日期','渠道','实际消耗','展示数','点击数','点击率']]

platform1['平台'] = '平台一'
platform2['平台'] = '平台二'

platform = platform1.copy()
platform = pd.concat([platform1,platform2],axis = 0)

