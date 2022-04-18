import smtplib #importing the module
from smtplib import SMTPResponseException 
from getpass import getpass
from decouple import config

def message(receiver_add, dataArray):
	
	sender_add='kadamchirag232001@gmail.com' #storing the sender's mail id
	password=str(config('KEY'))
	 #creating the SMTP server object by giving SMPT server address and port number
	try:
		smtp_server=smtplib.SMTP("smtp.gmail.com",587)
		smtp_server.ehlo() #setting the ESMTP protocol
		smtp_server.starttls() #setting up to TLS connection
		smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
		smtp_server.login(sender_add,password) #logging into out email id
		message = """From: Temp Sender <from@fromdomain.com>
		To: me <to@todomain.com>
		Subject: Admission Done

		On Current """+  dataArray[0] + """  Temperature at """+  dataArray[1] + """  is """+ dataArray[2] + """ and wind is """+  dataArray[3] + """ , Humidity is """+  dataArray[4] + """, Pressure is """+  dataArray[5] + """
        It Feels like """+  dataArray[6] + """ and """+  dataArray[7] + """
		""" 
		#sending the mail by specifying the from and to address and the message 
		smtp_server.sendmail(sender_add,receiver_add,message)
		# print('Successfully the mail is sent') #priting a message on sending the mail
	except SMTPResponseException as err:
		print('error : ', err)
	finally:
		smtp_server.quit()#terminating the server

# receiver_add = '20104034.chirag.padyal@gmail.com' #storing the receiver's mail id
# # password = str(config('KEY'))
# message(receiver_add, ["5" ,"5" ,"5" ,"5" ,"5" ,"5" ,"5" ,"5"])
