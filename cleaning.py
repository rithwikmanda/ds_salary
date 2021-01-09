# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:57:24 2021

@author: RITHWIK
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary min,max,avg

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)

#state only

df['job_state'] = df['Location'].apply(lambda  x: x.split(',')[1])

#age of company

df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#job description(terms)

df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R'] = df['Job Description'].apply(lambda x: 1 if ' R ' in x.upper() else 0)
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['azure'] = df['Job Description'].apply(lambda x: 1 if 'azure' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

df = df.drop(['Headquarters', 'Competitors'], axis=1)
df.to_csv('data_cleaned.csv', index=False)