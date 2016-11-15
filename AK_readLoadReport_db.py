# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:17:36 2015

@author: 105028218
"""

# -*- coding: utf-8 -*-
"""
Clean regression_report.txt
@author: 105028218
"""


import os.path
import datetime 
import time
import sqlite3 as lite
import sys
import csv


#FUNZIONI
def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sen', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1
    
def diff_dates(date1, date2):
    return abs(date2-date1).days
    

#DEFINIZIONI
filepath="C:\\Users\\105028218\\Desktop\\AccessKnowledge\\GE_Training_v_2_0\\Archives\\ak-solr-regression\\ak-pe-solr-regression\\regression_report\\regression_report.txt"
file = "regression_report.txt"
string1 = "CONTEXT ( "
string2 = "Total number"
string3 = "Last Updated"
con = lite.connect('test.db')
i=1
numline=0
numfound=0
z=14

print"****************************"
print" AK REFRESH REPORT"
print"****************************"



with open(filepath) as myfile:
    count = sum(1 for line in myfile)
count 

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS AK_REFRESH")
cur.execute("CREATE TABLE AK_REFRESH(SOURCE TEXT,RECORDS INT,LOAD DATE)")

infile = open(filepath,"r")
while z<count+120:
    z=z+1
    line=infile.readline()
    if line.find(string1) >= 0: 
        AA=line[line.find(string1)+10:-19]
    if line.find(string2) >= 0: 
        BB=line[line.find(")")+3:]
        BB=BB.rstrip()
    if line.find(string3) >= 0: 
        CC=line[line.find(")")+7:-19]
        CC=CC.rstrip()
        MESE=int(month_converter(CC[0:3]))
        DAY=int(CC[4:6])
        YEAR = datetime.datetime.now().year
        NOW = datetime.datetime.now()
        d= datetime.date(YEAR,MESE, DAY) 
        cur.execute("INSERT INTO AK_REFRESH values (?,?,?)",(AA,BB,d))

with con:
    cur = con.cursor()
    cur.execute("SELECT round(julianday('now')-julianday(LOAD),0),LOAD,RECORDS,SOURCE FROM AK_REFRESH order by 1 desc")
    rows = cur.fetchall()
    for row in rows:
        print row


with con:
    cur = con.cursor()
    cur.execute("SELECT count(1),sum(RECORDS) from AK_REFRESH")
    rows = cur.fetchall()
    for row in rows:
        print "SOURCES | TOTAL : "
        print row
        
print "UPDATED AD  : %s" % time.ctime(os.path.getmtime(filepath))

raw_input("Press Enter to continue...")