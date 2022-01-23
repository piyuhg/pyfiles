#!/usr/bin/python3
import smtplib
import getpass
username = input("Login ID: ")
password = getpass.getpass("Password: ",None)
receiver = input("Recipient Mail ID: ")
message = input("Enter Message: ")
try:
	server = smtplib.SMTP('smtp.gmail.com',587)	##setup SMTP
	server.ehlo()					##extended helo for client Indentification
	server.starttls()				#encrypting message at transport layers security telnet smtp
	server.login(username, password)
	server.sendmail(username, receiver, message)
	server.quit()
	print('Email Sent')
except ConnectionError:
	print("Failed to Send Mail \n Please Check Internet Connection ")
#except:
#	print("Exception occured..\n Retrying..")

