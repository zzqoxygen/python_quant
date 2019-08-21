# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:50:08 2019

@author: 72669
"""


#导入numpy
import numpy as np


a = np.arange(10)
type(a)
m = np.array([np.arange(10)])
print(m)
###切取第四至第六个元素（4，5，6号元素)，规则和原生的列表对象相似
print(m[3:7])
###以步长为2的方式选取元素
print(m[::3])