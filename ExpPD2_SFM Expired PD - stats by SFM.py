# -*- coding: utf-8 -*-
"""
Part II - split dataframe create XLS per each SFM , add empty formatted columns and send mails 
@author: 105028218
"""

import datetime
import numpy as np
import pandas as pd
from datetime import datetime

df_PO = pd.read_excel (r'C:\-FB-DATA-\_FB_Wk_Python\tmp1_EXP_PD\output.xlsx')
print(df_PO.info)

df_PO['PROMISED_DATE'] = pd.to_datetime(df_PO['PROMISED_DATE'])
df_PO['PROMISED_DATE_M'] = pd.to_datetime(df_PO['PROMISED_DATE']).dt.strftime('%Y')

groupvariable="PROMISED_DATE_M"
#groupvariable = 'SPA_MAIL'

#SFM =  df_PO[groupvariable].unique()
dftmp = df_PO[groupvariable].value_counts().sort_index()

#dftmp2  = pd.DataFrame(dftmp, columns = ['SPA_MAIL' , 'Count'])  #converte lista in dataframe
dftmp2  = pd.DataFrame(dftmp)  #converte lista in dataframe
dftmp2.reset_index(level=0, inplace=True)
dftmp2.columns = [groupvariable, 'Count']
dftmp2=dftmp2.sort_values(by=['Count'])
print(dftmp2) 
dftmp2.plot.bar(x=groupvariable,y='Count',figsize=(10,5))
