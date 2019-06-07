

# -*- coding: utf-8 -*-
"""
Oracle Recalled Docs Iteration

@author: 105028218
"""

import pandas as pd
import numpy as np
import os 
import sys
from pandas import DataFrame

PO1_List = pd.read_csv("PO_List.csv") 
PO2_List = pd.read_csv("ITEMJOB_List_v3.csv") 
print(PO1_List.size)
print(PO2_List.size)

print(os.getcwd())
path = "c:\\Temp\\"
sqlpath="c:\\-FB-DATA-\\_FB_Wk_Python\\"

os.environ['PATH'] = 'C:\Oracle\instantclient_18_5'
sys.path.append("c:\\users\\105028218\\box sync\\fb pc sync\\python\\venv\\lib\\site-packages")

import cx_Oracle as cx

con_PO = cx.connect('GEOG_SOU_SC/rfs4375tf@oscaroltp-db.og.ge.com:10110/oscaroltp')
df_PO1 = pd.DataFrame()
df_PO2 = pd.DataFrame()
sql_PO1 = sqlpath+'PoConfirm_param.sql'
sql_PO2 = sqlpath+'PO_RecalledDocs.sql'
i=0

#test connectionfor debug 
#print (con_PO.version)
#print (con_CYB.version)
#print (con_ITO.version)
#con.close()

def loadQuery(filename,connectname,df,Param1_old,Param1_new,Param2_old,Param2_new,dftarget,j):
    fd = open(filename, 'r')
    sqlname = fd.read()
    sqlname=sqlname.replace(Param1_old, Param1_new)
    sqlname=sqlname.replace(Param2_old, Param2_new)
    fd.close()  
    df = pd.read_sql(sqlname, connectname)
    KEY = Param1_new+"_"+Param2_new
    df['KEY']=(KEY)
    df.to_csv(KEY+".csv")
    print(str(j)+ " - "+KEY+".csv   records:" + str(df.size))
    
#def dataframe_analytics(df):
#    df1 = df.nunique()
#    df2 = len(df) - df.count()
#    df3 = df.count()
#    dfz=pd.concat([df1,df2,df3], axis=1)
#    dfz.columns = ['distinctvalues', 'null','notnull']
#    dfz['not_null_%']=(100*dfz['notnull']/len(df.index)).round(0).astype(str) + '%'
#    dfz.sort_values(by=['distinctvalues'], inplace=True, ascending=True)
#    print(dfz)
#    
#   


# LOOP FOR PO1 
#for index, row in PO1_List.iterrows():
#    i=i+1
#    ordernumber = str(row['PO'])
#    org = row['ORG']
#    loadQuery(sql_PO1,con_PO,df_PO1,"439073863",ordernumber,"OU_TD_FR",org,df_PO1,i)
#print("-"*50)


## LOOP FOR PO2
for index, row in PO2_List.iterrows():
     i=i+1
     ItemCode = row['ITEM']
     ProjectNumber = str(row['PROJ'])
     loadQuery(sql_PO2,con_PO,df_PO2,"2626M20G01",ItemCode,"1704043",ProjectNumber,df_PO2,i)

print("-"*50)
#loadQuery(sql_PO2,con_PO,df_PO2)
#dataframe_analytics(df_PO)

