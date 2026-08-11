#we want to send Automated Email using python by adding attachment(file)

import smtplib
import email
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#same include mailwith subject code
From='kankanalaakshitha2004@gmail.com'
To='prasannabont@gmail.com'
Subject='Email Automation using Python-Single user with Attachment'
app_password='xgci xyun adzt isbd'
body='In this project we will understand how python can be useful in real world applications'
attach='sample_email.py'#give your attachment name
msg=MIMEMultipart()
msg['From']
msg['To']
msg['Subject']=Subject
msg.attach(MIMEText(body))
#now we need to add file attachment
part=MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment;filename="%s" '%(os.path.basename(attach)))
msg.attach(part)
text=msg.as_string(part)
#start the server communction
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,app_password)
server.sendmail(From,To,text)
print("Mail Sent")
server.quit()