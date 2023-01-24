# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
# import environ


# env = environ.Env()

# text = 'You have created an account on our website'
# subject = 'Welcome to our service'
# username = 'pelumiv2023@gmail.com'
# app = env("GMAIL_APP_PASSWORD")
# receiver = 'abeniadeh18@gmail.com'
# sender = 'pelumiv2023@gmail.com'

# def send_email(text=text, subject=subject, from_email=sender, to_emails=[receiver]):
#     assert isinstance(to_emails, list)

#     msg=MIMEMultipart('alternative')
#     msg['From']=from_email
#     msg['To']=", ".join(to_emails)
#     msg['Subject']=subject
#     txt_part=MIMEText(text,'plain')
#     msg.attach(txt_part)
#     msg_str=msg.as_string()

#     server=smtplib.SMTP(host='smtp.gmail.com',port=587)
#     server.ehlo()
#     server.starttls()
#     server.login(username, app)
#     server.sendmail(from_email,to_emails, msg_str)
#     server.quit()
#     print('Send email')