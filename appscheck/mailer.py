from datetime import datetime

def mailer(sender, receiver, password, subject, html_msg):
	try:
		import smtplib

		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText

		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		msg['From'] = sender
		msg['To'] = receiver

		# Create the body of the message (a plain-text and an HTML version).
		text = "Welcome to Relevance lab, Application status on " + str(datetime.now()) + "\n\n"; 
		html = html_msg

		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		msg.attach(part1)
		msg.attach(part2)
		# Send the message via local SMTP server.
		mail = smtplib.SMTP('smtp.gmail.com', 587)

		mail.ehlo()

		mail.starttls()

		mail.login(sender, password)
		mail.sendmail(sender, receiver, msg.as_string())
		mail.quit()
		return True
	except smtplib.SMTPAuthenticationError as e:
		msg = "Properly specify the Email id and password and also make it accessible by less secure apps\n" + str(e)
		print msg 
		return False
	except Exception as e:
		print e
		return False