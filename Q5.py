#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:25:58 2022

@author: ml
"""

data = list(range(1,100))

import statistics

statistics.mean(data)
statistics.stdev(data)

print(statistics.mean(data))
print(statistics.stdev(data))
print(sum(data))