# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:29:30 2019
@author: fabio

REv 2019 
    aggiunto altro dottore
    scrive risultati su dataframe
    Regex per pulire risultato
    Email aggiunta in funzione esterna
"""

import urllib.request
import smtplib
import pandas as pd
import array 

TOFIND1 = 'di scelte'
TOFIND0_COGNOME = 'Cognome'
page = []
strpage = []

df = pd.DataFrame(columns=['DOTT','OUT'])

doctorsid= ['111468','319350','359174','20909','157800']
i = 0
while i < len(doctorsid):
    LINK= 'http://wiasf.cupmet-fi.it/ASFWeb/MMG/DettaglioMedici.do?medCod='+doctorsid[i]
    strpage.append(str(urllib.request.urlopen(LINK).read()))
    i += 1

x = 0
while x < len(doctorsid):
    ssfrom = strpage[x].find(TOFIND0_COGNOME)+55
    COGNOME = (strpage[x][ssfrom:ssfrom+10])
    COGNOME = COGNOME.split('<', 1)[0]
    ssfrom = strpage[x].find(TOFIND1)+57
    RESULT = (strpage[x][ssfrom:ssfrom+10])
    RESULT = RESULT.split('<', 1)[0]
    df.loc[x] = [COGNOME,RESULT]
    x += 1

print("--- ALL DOCTORS --- ")
print(df)
print("--- DOCTORS AVAILABLE --- ")

DoctorAvailable=  df['OUT']=='SI'
DoctorAvailabledf = df[DoctorAvailable]
print(DoctorAvailabledf.head())

if DoctorAvailabledf.size>1:
    from SendEmail import EMAIL
    too= "fabio.bertellotti@gmail.com"
    subjj = "PY Doctors found alert"
    msgg = DoctorAvailabledf.to_string()
    EMAIL(too,subjj,msgg)
