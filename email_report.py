#!/usr/bin/env python3

#####################################
#  Send an email with an attachment #
#####################################


import email.message
import mimetypes
import os.path
import smtplib

a_sender = ''
a_recipient = ''
a_subject = 'subject'
a_body = 'body'
a_attachment_path = '/path/to/attachment'
a_mail_pass = ''


# Creates an email with an optional attachment.
def generate_email(sender, recipient, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    # - Mime type indicates the nature and format of a document, file, or assortment of bytes
    attachment_filename = attachment_path
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_filename))
    return message

def send_email(e_message):
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    # Optional - mail_pass = getpass.getpass('')
    # With the getpass module can prompt the user for a password without echoing for security reasons
    mail_server.login(a_sender, a_mail_pass)
    mail_server.send_message(e_message)
    mail_server.quit()


message = generate_email(a_sender,a_recipient,a_subject,a_body,a_attachment_path)
send_email(message)
