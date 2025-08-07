#!/usr/bin/env python3

'''
1. Define generate_email and send_email methods by importing necessary libraries.
2. call the methods under the main method after creating the PDF report:

From: automation@example.com
To: student@example.com
Subject line: Upload Completed - Online Fruit Store
E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
Attachment: Attach the path to the file processed.pdf

'''
import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path=False):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Process the attachment and add it to the email
  if attachment_path:
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()