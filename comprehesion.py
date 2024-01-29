# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:46:37 2024

@author: 8086f
"""
li=['hello', "hi","sg"]
some_list=["a","b","c","d","b","m","n","n"]
print(li)
some=[i for i in some_list if some_list.count(i)>1 ]
print(some)
