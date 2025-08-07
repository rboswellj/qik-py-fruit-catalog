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

