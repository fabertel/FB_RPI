# -*- coding: utf-8 -*-
"""
Part II - split dataframe create XLS per each SFM , add empty formatted columns and send mails 
@author: 105028218
"""

import win32com.client
import datetime
import re
import numpy as np
import pandas as pd
from datetime import datetime
pd.options.mode.chained_assignment = None  # default='warn'
now = datetime.now()
d4 = now.strftime("%y%m%d_%H%M%S")
print("NOW =", d4)
print(df_PO.shape)

def isValidEmail(email):
 if len(email) > 7:
     if re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email) != None:
         return True
     return False
 
def SendMail(destinatario,soggetto,attachment1):
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.BodyFormat = olFormatPlain # Use for plain test
    newMail.Subject = soggetto
    newMail.To = destinatario
    newMail.Attachments.Add(attachment1)
    newMail.Send()

format1 = workbook.add_format({'num_format': '#,##0.00'})

#SFM =  df_PO['SPA_MAIL'].unique()
dftmp = df_PO['SPA_MAIL'].value_counts().sort_index()

u = 0

for i in SFM:  
#    i=i[:i.index("@")].replace('.', '')
    if i is not None : 
        if isValidEmail(i) == True :
             u=u+1 
#            if i =='alessio.campolmi@bhge.com' : 
             j=i[:i.index("@")].replace('.', '')
             tmpz = df_PO.loc[(df_PO['SPA_MAIL']==i)]
             tmpz ['New Promised Date'] = ''
             tmpz ['Justification'] = ''
             with pd.ExcelWriter(r'C:\-FB-DATA-\_FB_Wk_Python\tmp1_EXP_PD\ExpPD_'+d4+'_'+str(u)+'_'+str(j)+'.xlsx') as writer: 
                filename = 'ExpPD_'+d4+'_'+str(u)+'_'+str(j)+'.xlsx'
                tmpz.to_excel(writer, sheet_name='Sheet1')
                workbook  = writer.book
                worksheet = writer.sheets['Sheet1']
                #format3 = workbook.add_format({'num_format': '0%','bold': True,'color':'red'})
                format2 = workbook.add_format({'num_format': 'dd/mm/yy','bold': True,'color':'red'})
                format3 = workbook.add_format({'bold': True,'color':'red'})
                worksheet.set_column('BI:BI', 18, format3)
                worksheet.set_column('BJ:BJ', 18, format3)
                writer.save()
                attachment = 'C:\\-FB-DATA-\\_FB_Wk_Python\\tmp1_EXP_PD\\' + filename
                #print(attachment)
                SendMail("fabio.bertellotti@bhge.com",filename,attachment)
                print(str(u)+" "+filename)
        

#        else:
#            print ("NO")   


print("FINE")


#            
#for i in SFM:  
##    i=i[:i.index("@")].replace('.', '')
#    if i is not None : 
#        if isValidEmail(i) == True :
#         tmpz = df_PO.loc[(df_PO['SPA_NAME_FIXED']==i)]
#         with pd.ExcelWriter(r'C:\-FB-DATA-\_FB_Wk_Python\tmp1_EXP_PD\ExpPD_'+d4+'_'+str(i)+'.xlsx') as writer: 
#             tmpz.to_excel(writer, sheet_name='All')
#             print ('ExpPD_'+d4+str(i)+'.xlsx')
##        else:
##            print ("NO")   
#
#         



    
