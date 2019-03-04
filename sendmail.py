import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "sgb@mail.com"
you = "target@mail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Forgot Password"
msg['From'] = me
msg['To'] = you

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.sgb.or.id"
html = open('letter.html').read()

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login('sgb@mail.com', 'password_you')
smtpserver.sendmail(me, you, msg.as_string())
smtpserver.quit()