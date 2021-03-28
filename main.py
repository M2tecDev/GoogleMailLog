import smtplib

# https://myaccount.google.com/lesssecureapps
# wenn das senden nicht geht muss das umgestellt werden 
# https://i.stack.imgur.com/1yPnO.png

# Settings
gMail_Name = "log_Server@gmail.com" # Server Email 
gMail_Password = "SuperSecurePassword" # Password

def SendMail(sub, body):

    # Sender Settings
    send_from = gMail_Name
    send_to = ['administrator@gmail.com', 'Developer@gmail.com'] # You can add more here
    send_subject = sub
    send_body = body

    email_text="""\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (send_from, " , ".join(send_to), send_subject, send_body)
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gMail_Name, gMail_Password)
        server.sendmail(send_from, send_to, email_text)
        server.close()
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

SendMail("Ein Fehler ist aufgetreten", "Python.py Function: def Python\nLine: 88")
