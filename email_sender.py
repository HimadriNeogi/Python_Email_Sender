import smtplib
import copy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

# Email Credentials
email_ids = ["test_recipient1@gmail.com", "test_recipient2@gmail.com"]  # add all the recipient email address
subject = "Email Automation Test"  # add subject
with open ("email_body.txt", "r") as file:  # add the body of the email
    body = file.read()
sender_id = "your_email@gmail.com"  # add sender email address
sender_pw = "your_app_password"  # add password (not your gmail password)

# Add attachment
with open("your-file.pdf", 'rb') as f:  # add the attachment
    attachment = MIMEApplication(f.read(), Name="your-file.pdf")

attachment["Content-Disposition"] = f'attachment; filename="your-file.pdf"'  # attachment header

# SMTP connection
server = smtplib.SMTP("smtp.gmail.com", 587)  # use port 587 to establish a secure connection using TLS
server.starttls()
server.login(sender_id, sender_pw)

# Email setup
for recipient in email_ids:
    msg = MIMEMultipart()
    msg["From"] = sender_id
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    msg.attach(copy.deepcopy(attachment))
    try:
        server.sendmail(sender_id, recipient, msg.as_string())
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

server.quit()