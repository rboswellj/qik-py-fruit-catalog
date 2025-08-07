#!/usr/bin/env python3

'''
1. process text files from supplier-data/descriptions
2. Turn the data into a JSON dictionary
    a. Name
    b. Weight
    c. Description
    d. image associated with the fruit (image_name)
3. upload it to http://[external-IP-address]/fruits using the Python requests library.
'''

import os
import requests

