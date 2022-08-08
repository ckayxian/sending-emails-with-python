# Email Sender

## Overview
This application allows users to send email with Python and the SMTP (Simple Mail Transfer Protocol) library
Users can customize subject line, recipient's email address and name

## Installation
SMTP is a built-in module, so there's no installation required

## Try It Out
1. Modify `email["from"] = "<Sender's name>"` with the name of person who is sending out this email
2. Modify `email["to"] = "<Recipient's email address>"` with the email address of the person who receives this email
3. Modify `email["subject"] = "<Subject Line>"` with your customized subject line
4. Modify `email.set_content(html.substitute({"name": "<Recipient's name>"}), "html")` with recipient's name
5. Modify `smtp.login("<Sender's email address>", "<Sender's password>")` with sender's email address and password

### Note
You will need to go to your Gmail account > Account Setting > Scroll to the bottom and turn on the **Less Secure Apps** tab
in order to send email with this application.
You can turn this tab back **OFF** to ensure your account's safety after using this application