import smtplib
from email.mime.text import MIMEText

class PyMailer:
  def __init__(self, array):
    self.smtp_host = array['smtp_host']
    self.smtp_port = array['smtp_port']
    self.email = array['email']
    self.password = array['password']
    self.to = array['to']
    self.subject = array['subject']
    self.body = array['body']
    self.display = array['display']
    
  def send(self):
    msg = MIMEText(self.body, 'html')
    msg['From'] = self.email
    msg['To'] = self.to
    msg['Subject'] = self.subject
    
    with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
      smtp.starttls()
      smtp.login(self.email, self.password)
      smtp.send_message(msg)
      if self.display:
        print(f"""SMTP Host : {self.smtp_host}
SMTP Port : {self.smtp_port}
Email : {self.email}
Password : {self.password}
To : {self.to}
Subject : {self.subject}
Body : {self.body}\n\n
Email sent successfully.""")
