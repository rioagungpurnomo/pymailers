import smtplib
import sys
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
    
    try:
      with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
        smtp.starttls()
    except Exception:
      print("SMTP Host and SMTP Port error occurred.")
      sys.exit()
    try:
        smtp.login(self.email, self.password)
        smtp.send_message(msg)
        if self.display:
          print(f"""SMTP Host : {self.smtp_host}
          SMTP Port : {self.smtp_port}
          Email : {self.email}
          To : {self.to}
          Subject : {self.subject}
          Body : {self.body}\n
          Email sent successfully.""")
    except Exception:
      ep = "if the email is correct, your password is wrong."
      print(f"Check your email and password again, {ep}")