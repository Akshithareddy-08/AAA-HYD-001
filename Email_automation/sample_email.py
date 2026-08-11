#setp1:-->setting up Gmail app password
we will use SMPT(sample mail transfer protocol)
#step2:-->using SMTPLIB we start the communction

import smtplib 
#first we will make the protocal connection
server=smtplib.SMTP('smtp.gmail.com',587)
print(server)
#start communication
server.starttls()
#we will make the login
server.login('kankanalaakshitha2004@gmail.com','xgci xyun adzt isbd')
print('login Success')
message='Welcome to my World..This is an Automated Mail...'
#send the mail
server.sendmail('kankanalaakshitha2004@gmail.com','prasannabont@gmail.com',message)
print('Success')
