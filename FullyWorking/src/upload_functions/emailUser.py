import smtplib

'''
EMAIL_TO
EMAIL_PASSWORD
EMAIL_SERVER
EMAIL_SERVER_PORT
'''
# Stage 2c: Email User alert that new repo has been created, document the Repo Link, CVEID and CanaryToken ID
def emailUser(cve, EMAIL_TO, EMAIL_PASSWORD, EMAIL_SERVER, EMAIL_SERVER_PORT):
    # Change this to free form
    TO = EMAIL_TO
    SUBJECT = f'CVE Mailer {cve}'
    TEXT = f'New Github Repo Created for {cve} and a pastebin link has also been created'
    # Email Sign In
    sender = EMAIL_TO
    password = EMAIL_PASSWORD
    server = smtplib.SMTP(EMAIL_SERVER, EMAIL_SERVER_PORT)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    try:
        server.sendmail(sender, [TO], BODY)
        print (f'Email Sent to {TO}')
    except:
        print (f'Error Sending Mail to {TO}')
    server.quit()
