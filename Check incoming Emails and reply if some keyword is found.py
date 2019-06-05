# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:11:05 2019

@author: 105028218
"""

#print(os.getcwd())

import datetime
import win32com.client
import time
import sys
import datetime as dt

sys.path.append("c:\\users\\105028218\\box sync\\fb pc sync\\python\\venv\\lib\\site-packages")


def sendmail(Subjecttt):
    obj = win32com.client.Dispatch("Outlook.Application")
    olMailItem = 0x0
    olFormatUnspecified = 0x00
    olFormatPlain = 0x01
    olFormatHTML = 0x02
    olFormatRichText = 0x03
    newMail = obj.CreateItem(olMailItem)
    newMail.BodyFormat = olFormatPlain # Use for plain test
    newMail.Subject = Subjecttt
    newMail.To = "fabio.bertellotti@bhge.com"
    # Note: If sending HTML format use newMail.HTMLBody = and provide valid html as the body
    #       you can attach both plain text and html versions to HTML format messages.
    newMail.Body = "a new mail on RPA was received" 
    newMail.Send()


date_time = dt.datetime.now()
lastHourDateTime = dt.datetime.now() - dt.timedelta(hours = 1)
last10HourDateTime = dt.datetime.now() - dt.timedelta(hours = 10)
lastMinuteDateTime = dt.datetime.now() - dt.timedelta(minutes = 1)

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
messages = inbox.Items
messages.Sort("[ReceivedTime]", True)
#print(messages.count)

lastHourMessages = messages.Restrict("[ReceivedTime] >= '" +lastHourDateTime.strftime('%m/%d/%Y %H:%M %p')+"'")
last10HourMessages = messages.Restrict("[ReceivedTime] >= '" +last10HourDateTime.strftime('%m/%d/%Y %H:%M %p')+"'")
HourMessages = messages.Restrict("[ReceivedTime] >= '" +lastHourDateTime.strftime('%m/%d/%Y %H:%M %p')+"'")
lastMinuteMessages = messages.Restrict("[ReceivedTime] >= '" +lastMinuteDateTime.strftime('%m/%d/%Y %H:%M %p')+"'")



# NOTIFIES MAIL WITH AK 
keyword = "AK"

for message in last10HourMessages:
    if keyword in message.Subject :
#        print(message.subject+ message.ReceivedTime.strftime('%m/%d/%Y %H:%M %p'))
        sendmail("NEWMAIL : " + message.subject+ message.ReceivedTime.strftime('%m/%d/%Y %H:%M %p'))


##CHECK MAILS RECEIVED IN TIMEFRAMES 
#print ("Current time: "+date_time.strftime('%m/%d/%Y %H:%M %p'))
#print ("----------------")
#print ("last10HourMessages :"+ str(last10HourMessages.count))
#for message in last10HourMessages:
#    print (message.subject+ message.ReceivedTime.strftime('%m/%d/%Y %H:%M %p'))

##print ("----------------")
#print ("lastMinuteMessages :"+ str(lastMinuteMessages.count))
#for message in lastMinuteMessages:
#    print (message.subject+ message.ReceivedTime.strftime('%m/%d/%Y %H:%M %p'))
#    
#print ("----------------")
#print ("Using GetFirst/GetNext")
#message = lastHourMessages.GetFirst()
#while message:
#    print (message.subject+ message.ReceivedTime.strftime('%m/%d/%Y %H:%M %p'))
#    message = lastHourMessages.GetNext()
    
    
    
##-----------------------------------------------
#LAST MAIL 
#
#message = messages.GetLast()
#body_content = message.body
#print(body_content)
#-----------------------------------------------
#FILTER BY CONTENT
#
#i=0
#for m in messages:
#    if "RPA" in m.Subject :
#           i=i+1
#
#print (i)
#-----------------------------------------------
#REFRESH LIST OF FOLDERS
#
#import win32com
#outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#for i in range(20):
#    try:
#        box = outlook.GetDefaultFolder(i)
#        name = box.Name
#        print(i, name)
#    except:
#        pass
#LIST OF FOLDERS
#3 Posta eliminata
#4 Posta in uscita
#5 Posta inviata
#6 Inbox
#9 Calendario
#10 Contatti
#11 Journal
#12 Note
#13 Attività
#14 Reminders
#15 Reminders
#16 Bozze
#17 Conflitti
#19 Conflitti