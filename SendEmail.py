
# Funzione per mandare mail.nel codice servono queste 4 righesotto

#from SendEmail import EMAIL
#too= "fabio.bertellotti@gmail.com"
#subjj = "Auto alert"
#msgg = "warning"
#EMAIL(too,subjj,msgg)


import email
import smtplib

def EMAIL(TO,SUBJ,BODY):
    msg = email.message_from_string(BODY)
    msg['From'] = "fabio.bertellotti@hotmail.com"
    msg['To'] = TO
    msg['Subject'] = SUBJ
    passw = 'WWW222www'
    
    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls() #Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login(msg['From'], passw)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    print("mail sent")
    
