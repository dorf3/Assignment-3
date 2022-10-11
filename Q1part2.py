#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:12:18 2022

@author: ml
"""


from statistics import mean

marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur': 77}
avg_score = mean(marks.values())
print(avg_score)