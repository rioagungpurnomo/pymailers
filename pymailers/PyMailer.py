import smtplib
from sys import exit as logout
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
    self.success = f"{self.WHITE}[{self.GREEN}!{self.WHITE}]"
    self.failed = f"{self.WHITE}[{self.RED}!{self.WHITE}]"
    self.message_smtp = "SMTP Host and SMTP Port error occurred."
    self.message_passwprd = "SMTP Host and SMTP Port error occurred."
    
  def send(self):
    msg = MIMEText(self.body, 'html')
    msg['From'] = self.email
    msg['To'] = self.to
    msg['Subject'] = self.subject
    
    try:
      with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
        smtp.starttls()
    except Exception:
      logout(print(f"""\n{self.failed} {self.message_smtp}{self.DEFAULT}"""))
    try:
        smtp.login(self.email, self.password)
        smtp.send_message(msg)
        if self.display:
          print(f"""\n{self.WHITE}SMTP Host : {self.smtp_host}
          SMTP Port : {self.smtp_port}
          Email : {self.email}
          To : {self.to}
          Subject : {self.subject}
          Body : {self.body}\n
          {self.success} Email sent successfully.{self.DEFAULT}""")
    except Exception:
      logout(print(f"""\n{self.failed} {self.message}{self.DEFAULT}"""))