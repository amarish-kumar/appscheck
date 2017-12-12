# import smtplib
# fromaddr = 'rishikesh0014051992@gmail.com'
# toaddrs  = 'rishikesh.agrawani@relevancelab.com'


# msg = 'Why,Oh why!'
# username = 'rishikesh0014051992@gmail.com'
# password = 'Hygull_67'

# server = smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo()
# server.starttls()
# server.login(username,password)
# server.sendmail(fromaddr, toaddrs, msg)
# server.quit()

# def send_email(user, pwd, recipient, subject, body):
#     import smtplib

#     gmail_user = user
#     gmail_pwd = pwd
#     FROM = user
#     TO = recipient if type(recipient) is list else [recipient]
#     SUBJECT = subject
#     TEXT = body

#     # Prepare actual message
#     message = """From: %s\nTo: %s\nSubject: %s\n\n%s
#     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.login(gmail_user, gmail_pwd)
#         server.sendmail(FROM, TO, message)
#         server.close()
#         print 'successfully sent the mail'
#     except:
#         print "failed to send mail"

# send_email("rishikesh0014051992@gmail.com", "Hygull_67", "rishidev-rel@crymail2.com", "APPLICATION STATUS", "Welcome")

try:
	import smtplib

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# me == my email address
	# you == recipient's email address
	me = "rishikesh0014051992@gmail.com"
	you = "rishidev-rel@crymail2.com"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Hi!<br>

	       How are you?<br>
	       Here is the <a href="http://www.python.org">link</a> you wanted.
	    </p>
	  </body>
	</html>
	"""

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

	mail.login('rishikesh0014051992@gmail.com', 'Hygul_6')
	mail.sendmail(me, you, msg.as_string())
	mail.quit()
except smtplib.SMTPAuthenticationError as e:
	print "Properly specify the Email id and password and also make it accessible by less secure apps\n", e