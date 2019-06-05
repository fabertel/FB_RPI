# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 01:18:25 2019

INTERESSANTE 
> connette a Gmail
> scarica labels 
> conta mail con una label 

DA FINIRE : estrazione mails 

#NEEDS Less secure app access = ON
#https://myaccount.google.com/lesssecureapps?utm_source=google-account&utm_medium=web

@author: fabio
"""



import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('fabio.bertellotti@gmail.com', 'EEE333eee')

mailboxes = mail.list()

# LSIT MAILBOXES
#for mailbox in mailboxes:
#    print(mailbox.decode("utf-8"))

mail.list() # Lists all labels in GMail
mail.select('VIAGGI/KO17') # Connected to inbox.

selected = mail.select('VIAGGI/KO17')
messageCount = int(selected[1][0])
print(messageCount)

# DA FINIRE 

#resp, data = mail.uid('FETCH', ','.join(map(str,uidl_list)) , '(BODY.PEEK[HEADER.FIELDS (From Subject)] RFC822.SIZE)')

#typ, data = mail.search(None, 'ALL')
#for num in data[0].split():
#    typ, data = mail.fetch(num, '(RFC822)')
#    print('Message %s\n%s\n' % (num, data[0][1]))
#mail.close()
#mail.logout()

#def parse_header(str_after, checkli_name, mailbox) :
#    #typ, data = m.search(None,'SENTON', str_after)
#    print mailbox
#    m.SELECT(mailbox)
#    date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
#    #date = (datetime.date.today().strftime("%d-%b-%Y"))
#    #date = "23-Jul-2012"
#
#    print date
#    result, data = m.uid('search', None, '(SENTON %s)' % date)
#    print data
#
#    doneli = []
#    for latest_email_uid in data[0].split():
#        print latest_email_uid
#        result, data = m.uid('fetch', latest_email_uid, '(RFC822)')
#        raw_email = data[0][1]
#
#        import email
#        email_message = email.message_from_string(raw_email)
#        print email_message['To']
#        print email_message['Subject']
#        print email.utils.parseaddr(email_message['From'])
#        print email_message.items() # print all headers
#        
#        


#  for i in range(messageCount, messageCount - top, -1):
#    reponse = mailbox.fetch(str(i), '(RFC822)')[1]
#    for part in reponse:
#      if isinstance(part, tuple):
#        message = email.message_from_string(part[1])
#        yield {h: decodeHeader(message[h]) for h in ('subject', 'from', 'date')}
#
#  mailbox.logout()

