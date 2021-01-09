# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:59:29 2021

@author: RITHWIK
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/RITHWIK/Desktop/ds_salary/chromedriver"

df = gs.get_jobs('data scientist',10000,False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)