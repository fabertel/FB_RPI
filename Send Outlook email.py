# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:10:29 2019
Send mail from Outlook from PC default Account 
@author: 105028218
"""

import win32com.client
import datetime

obj = win32com.client.Dispatch("Outlook.Application")
olMailItem = 0x0
olFormatUnspecified = 0x00
olFormatPlain = 0x01
olFormatHTML = 0x02
olFormatRichText = 0x03
newMail = obj.CreateItem(olMailItem)
newMail.BodyFormat = olFormatPlain # Use for plain test
newMail.Subject = "Test Python Outlook Mail"
newMail.To = "fabio.bertellotti@bhge.com"
# Note: If sending HTML format use newMail.HTMLBody = and provide valid html as the body
#       you can attach both plain text and html versions to HTML format messages.
newMail.Subject = ("AUTO " + str(datetime.datetime.now().strftime('%m/%d/%Y %H:%M %p')))
newMail.Send()


