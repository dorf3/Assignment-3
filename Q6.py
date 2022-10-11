#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:41:01 2022

@author: ml
"""

def func_minimum(value1, value2, value3, value4):
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value

func_minimum(80, 34, 56, 78)
print(func_minimum(80, 34, 56, 78))


    
    