#!/usr/bin/env python3

'''
1. Import the necessary Python libraries (eg. shutil, psutil)
2. check the system statistics every 60 seconds
    a. Report an error if CPU usage is over 80%
    b. Report an error if available disk space is lower than 20%
    c. Report an error if available memory is less than 100MB
    d. Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
3. If any of the above checks fail, send an email to the system administrator
'''

#!/usr/bin/env python3
import shutil
import psutil
import socket
import smtplib
from email.message import EmailMessage 

def check_system_stats():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        return "Error - CPU usage is over 80%"

    # Check available disk space
    disk_usage = shutil.disk_usage('/')
    free_disk_space = disk_usage.free / (1024 * 1024 * 1024)  # Convert to GB
    if free_disk_space < 20:
        return "Error - Available disk space is less than 20%"

    # Check available memory
    memory_info = psutil.virtual_memory()
    if memory_info.available < 100 * 1024 * 1024:  # Less than 100 MB
        return "Error - Available memory is less than 100MB"

    # Check hostname resolution
    try:
        socket.gethostbyname("localhost")
    except socket.error:
        return "Error - localhost cannot be resolved to 127.0.0.1"
    
    return None

def generate_email(sender, recipient, subject, body):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)


  return message

def send_email(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

if __name__ == "__main__":
    # Define email parameters
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    subject = check_system_stats()
    
    if check_system_stats() != None:
        print("System check failed. Sending email notification.")
    