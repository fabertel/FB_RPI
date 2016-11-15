# -*- coding: utf-8 -*-
"""
Clean regression_report.txt
@author: 105028218
"""

 
import os.path
import datetime 
import time

def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sen', 'Oct', 'Nov', 'Dec']
    return months.index(month) + 1
    
def diff_dates(date1, date2):
    return abs(date2-date1).days
    
    
filepath="C:\\Users\\105028218\\Desktop\\AccessKnowledge\\GE_Training_v_2_0\\Archives\\ak-solr-regression\\ak-pe-solr-regression\\regression_report\\regression_report.txt"
file = "regression_report.txt"
string1 = "CONTEXT ( "
string2 = "Total number"
string3 = "Last Updated"
#file=input("enter the name of the file")
#string=input("enter the string you want to find")

with open(filepath) as myfile:
    count = sum(1 for line in myfile)
count 


numline=0
numfound=0
z=14

infile = open(filepath,"r")
while z<count+20:
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
       # DELAY = diff_dates(NOW,d)
        print BB, "\t",d,"\t",AA

time.sleep(5)

