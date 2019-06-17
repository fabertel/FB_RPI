# -*- coding: utf-8 -*-
"""
Run Oracle Query and save query to DF

@author: 105028218
"""


import pandas as pd
import os 
import sys

print(os.getcwd())

path = "c:\\Temp\\"
os.environ['PATH'] = 'C:\Oracle\instantclient_18_5'
sys.path.append("c:\\users\\105028218\\box sync\\fb pc sync\\python\\venv\\lib\\site-packages")

import cx_Oracle as cx

con_PO = cx.connect('GEOG_SOU_SC/rfs4375tf@oscaroltp-db.og.ge.com:10110/oscaroltp')
con_CYB = cx.connect('APPSV/VAPPS@ogoelamsdbp-scan.og.ge.com:1521/ORPOGOP6')
con_CDI = cx.connect('APPSV/VAPPS@ogoelamsdbp-scan.og.ge.com:1521/ORPOGOP6')
con_DWH = cx.connect('SSO105028218/Fab_123s@argo-prod-db.og.ge.com:10110/POGG1O')
con_ITO = cx.connect('SSO105028218/S23dS23dS23d@ogtmflitptcdb01.corporate.ge.com:1521/ONNTMP10')

## Check connection
#print (con_CDI.version)
#con.close()

fd = open('Expired_PD_sql_Bot.sql', 'r')
sql = fd.read()
fd.close()

df_PO = pd.read_sql(sql, con_DWH)
print(df_PO.shape)
#

with pd.ExcelWriter(r'C:\-FB-DATA-\_FB_Wk_Python\tmp1_EXP_PD\output.xlsx') as writer: 
    df_PO.to_excel(writer, sheet_name='All')

print("fine")


#with con:
#    cur = con.cursor()
#    cur.execute(sql_PO)
#    rows = cur.fetchall()
#    df = pd.read_sql(sql_PO, con)
#    print(df.shape)