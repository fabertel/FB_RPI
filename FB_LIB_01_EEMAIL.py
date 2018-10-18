import smtplib

def EEMAIL(SUBJECT,TEXT):
    msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
    fromaddr = 'fabio.bertellotti@gmail.com'
    toaddrs  = 'fabio.bertellotti@gmail.com'
    username = 'fabio.bertellotti@gmail.com'
    password = 'EEE333eee'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

EEMAIL('a','b')