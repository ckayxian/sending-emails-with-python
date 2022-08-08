import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email["from"] = "<Sender's name>"
email["to"] = "<Recipient's email address>"
email["subject"] = "<Subject Line>"

email.set_content(html.substitute({"name": "<Recipient's name>"}), "html")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("<Sender's email address>", "<Sender's password>")
    smtp.send_message(email)
    print("Email was sent!")