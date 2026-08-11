
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#give from address,to address and subject
From='kankanalaakshitha2004@gmail.com'
To='prasannabont@gmail.com'
Subject='Agentic AI Classes'
msg=MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
body='keep it up,grow more,get a job as soon as possible'
msg.attach(MIMEText(body))
#enter message to string format
text=msg.as_string()
#same as previous SMTP usage we will follow
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('kankanalaakshitha2004@gmail.com','xgci xyun adzt isbd')
server.sendmail(From,To,text)
print('Mail Sent')
server.quit()

#send OTP to user and validate it
import smtplib
import email
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#give from address,to address and subject
From='manimalanama24@gmail.com'
To='prasannabont@gmail.com'
Subject='Agentic AI Classes'
msg=MIMEMultipart()
msg['From']=From
msg['To']=To
msg['Subject']=Subject
otp=random.randint(1000,9999)
body=f'the otp is{otp}'
msg.attach(MIMEText(body))
#enter message to string format
text=msg.as_string()
#same as previous SMTP usage we will follow
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('kankanalaakshitha2004@gmail.com','xgci xyun adzt isbd')
server.sendmail(From,To,text)
print('Mail Sent')
a=int(input('Enter the OTP:'))
if a==otp:
    print(f'Login Success')
else:
    print('Login Failed')
    