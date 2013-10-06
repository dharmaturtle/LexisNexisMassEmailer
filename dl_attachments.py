#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This cycles through all the emails in an address, downloading the attachments, saving them under a randomly generated filename, then deleting the email.
Running rename.py will parse all the documents and rename them according to their contents.

http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
'''

import email, imaplib, os, sys, traceback, random, string

userName = "username goes here"
passwd = "password goes here"
print userName
detach_dir = '.'
if userName not in os.listdir(detach_dir):
	os.mkdir(userName)

imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login(userName, passwd)
if typ != 'OK':
	print 'Not able to sign in!'

imapSession.select('[Gmail]/All Mail')
typ, data = imapSession.search(None, 'ALL')
if typ != 'OK':
	print 'Error searching Inbox.'

# Iterating over all emails
mess_no = 0
j = 0
for msgId in data[0].split():
	try:
		typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
		if typ != 'OK':
			print 'Error fetching mail.'
			raise

		emailBody = messageParts[0][1]
		mail = email.message_from_string(emailBody)
		for part in mail.walk():
			try:
				j += 1
				if part.get_content_maintype() == 'multipart':
					#print part.as_string()
					continue
				if part.get('Content-Disposition') is None:
					#print part.as_string()
					continue
				fileName = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(100))
				fileName = fileName + ".txt"
				if bool(fileName):
					filePath = os.path.join("..", "day", fileName)
					if not os.path.isfile(filePath) :
						fp = open(filePath, 'wb')
						aaa = part.get_payload(decode=True)
						fp.write(aaa)
						fp.close()
						i = 0
					else:
						try:
							i += 1
							s = fileName.rsplit('.',1)
							fileName = s[0] + " (" + str(i) + ")." + s[1]
							fp = open(filePath, 'wb')
							fp.write(part.get_payload(decode=True))
							fp.close()
						except:
							s = fileName.rsplit('.',1)
							fileName = s[0] + " duplicate(" + str(j) + ")." + s[1]
							fp = open(filePath, 'wb')
							fp.write(part.get_payload(decode=True))
							fp.close()
			except (KeyboardInterrupt, SystemExit):
				raise
			except:
				traceback.print_tb(sys.exc_info()[2])
				print str(sys.exc_info())
				print "Inner loop\n"
		mess_no += 1
		imapSession.store(mess_no,'+X-GM-LABELS', '\\Trash')
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_tb(sys.exc_info()[2])
		print str(sys.exc_info())
		print "Outer loop\n"
imapSession.expunge()
imapSession.close()
imapSession.logout()