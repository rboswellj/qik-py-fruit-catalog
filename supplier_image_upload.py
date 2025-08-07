#!/usr/bin/env python3

'''
Takes images from supplier-data/images
Uploads them to web server
'''

import requests
import os


# Takes in directory
def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg'):
            upload_image(os.path.join(directory, filename))

def upload_image(image_path):
    with open(image_path, 'rb') as img_file:
        file = {'file': img_file}
        response = requests.post(url, files=file)
        if response.status_code == 201:
            print(f"Uploaded {image_path} successfully.")
        else:
            print(f"Failed to upload {image_path}. Status code: {response.status_code}")

url = "http://localhost/upload/"
img_directory = './supplier-data/images' 

process_directory(img_directory)
print("Image upload complete.")


