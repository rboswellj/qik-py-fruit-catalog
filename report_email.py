#!/usr/bin/env python3

''' 
emails a report when the fruit upload is complete
'''
import datetime
from run import process_directory
from emails import generate_email, send
from reports import generate_report

if __name__ == "__main__":
    # Define email parameters
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    # Define the report filename and title
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    report_filename = "processed.pdf"
    report_title = "Processed Update on {}".format(current_date)

    # Uses the dictionary builder from run.py 
    report_body = process_directory('./supplier-data/descriptions')
    generate_report(report_filename, report_title, report_body)

    attachment = "./processed.pdf"  # Path to the report file

    email_message = generate_email(sender, recipient, subject, body, attachment)
    send(email_message)

