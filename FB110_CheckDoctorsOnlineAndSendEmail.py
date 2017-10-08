import urllib.request
import smtplib

def EEMAIL(SUBJECT,TEXT):
    msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
    fromaddr = 'fabio.bertellotti@gmail.com'
    toaddrs  = 'fabio.bertellotti@gmail.com'
    username = 'fabio.bertellotti@gmail.com'
    password = 'cinghiale3'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

TOFIND1 = 'di scelte'
TOFIND0_COGNOME = 'Cognome'
i = 3
page = []
strpage = []
COGN = []
OUT = []
emailtrigger = 0 

strpage.append(str(urllib.request.urlopen('http://wiasf.cupmet-fi.it/ASFWeb/MMG/DettaglioMedici.do?medCod=111468').read()))
strpage.append(str(urllib.request.urlopen('http://wiasf.cupmet-fi.it/ASFWeb/MMG/DettaglioMedici.do?medCod=319350').read()))
strpage.append(str(urllib.request.urlopen('http://wiasf.cupmet-fi.it/ASFWeb/MMG/DettaglioMedici.do?medCod=359174').read()))

for x in range(0, 3):
    ssfrom = strpage[x].find(TOFIND0_COGNOME)+55
    COGN.append(strpage[x][ssfrom:ssfrom+10])
    ssfrom = strpage[x].find(TOFIND1)+57
    OUT.append(strpage[x][ssfrom:ssfrom+10])

ALL = COGN + OUT 
print (ALL)

for x in range(0, 3):
    if 'SI</label>' in OUT[x]:
        emailtrigger = 1 
        print(COGN[x],OUT[x])
    else :
        print(COGN[x],'no')

if emailtrigger==1 : 
    print(emailtrigger)
    EEMAIL('Doctor Found',ALL)