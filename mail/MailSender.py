#!/usr/bin/env python
import smtplib

from email import encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Email(object):

    def __init__(self, emailProperty):
        self.emailProperty = emailProperty

    def init_connection(self):
        try:
            session = smtplib.SMTP(self.emailProperty.server, self.emailProperty.port)
            session.ehlo()
            session.starttls()
            session.ehlo
            session.login(self.emailProperty.fromEmail, self.emailProperty.password)
            return session
        except Exception, e:
            print str(e)

    def close_connection(self, session):
        try:
            session.close()
            session.quit()
        except Exception, e:
            print str(e)

    def send_message(self, session, toEmail, subject, body, attachment):
        msg = MIMEMultipart()
        msg['From'] = self.emailProperty.fromEmail
        msg['To'] = toEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(attachment)
        try:
            session.sendmail(self.emailProperty.fromEmail, toEmail, msg.as_string())
        except Exception, e:
            print str(e)

    def load_Attachements(self, attachmentFileName):
        attachment = open(attachmentFileName, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachmentFileName)
        return part
