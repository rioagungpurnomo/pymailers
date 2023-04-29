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
    self.WHITE = '\x1b[1;97m'
    self.RED = '\x1b[1;91m'
    self.GREEN = '\x1b[1;92m'
    self.YELLOW = '\x1b[1;93m'
    self.PURPLE = '\x1b[1;94m'
    self.BLUE = '\x1b[1;96m'
    self.DEFAULT = '\x1b[0m'
    
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
{self.WHITE}SMTP Port : {self.smtp_port}
Email : {self.email}
To : {self.to}
Subject : {self.subject}
Body : {self.body}\n\n
{self.GREEN}Email sent successfully.{self.DEFAULT}""")
