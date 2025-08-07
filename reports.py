#!/usr/bin/env python3

'''
1. Create a PDF report of the updates
'''
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from run import process_directory

import datetime

def generate(filename, title, body_dict):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  body = []
  for item in body_dict:  # Assuming body_dict is a list of dictionaries
    body.append(Paragraph("name: {}".format(item['name']), styles["BodyText"]))
    body.append(Paragraph("weight: {} lbs".format(item['weight']), styles["BodyText"]))
    body.append(Spacer(1,20))
     
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, *body])

if __name__ == "__main__":
    # Define the report filename and title
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_filename = "processed.pdf"
    report_title = "Processed Update on {}".format(current_date)

    # Uses the dictionary builder from run.py 
    body = process_directory('./supplier-data/descriptions')
    
    # Generate the report
    generate(report_filename, report_title, body)
    print(f"Report generated: {report_filename}")