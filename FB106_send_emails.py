# versione facile ma funziona .. provare commando EMAIL 
import smtplib

SUBJECT = 'titolo email2'
TEXT = 'tuerytyuklhoklk'
msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)

fromaddr = 'fabio.bertellotti@gmail.com'
toaddrs  = 'fabio.bertellotti@gmail.com'


# Credentials (if needed)
# username = 'fabio.bertellotti@gmail.com'
# password = 'cinghiale3'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

