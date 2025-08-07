#!/usr/bin/env python3

'''
1. process text files from supplier-data/descriptions
2. Turn the data into a JSON dictionary
    a. name
    b. weight
    c. description
    d. image_name
3. upload it to http://[external-IP-address]/fruits using the Python requests library.
'''

import os
import requests

def process_file(file_path):
    fruit = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                fruit['name'] = lines[0].strip()
                fruit['weight'] = int(lines[1].strip().split()[0])  # Extract number before 'lbs'
                fruit['description'] = lines[2].strip()
                fruit['image_name'] = os.path.basename(file_path).replace('.txt', '.jpeg')
            else:
                print(f"File {file_path} does not contain enough lines.")
                return None
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

    # Upload the fruit data to the server
    url = "http://localhost/fruits/"
    try:
        response = requests.post(url, json=fruit)
        if response.status_code == 201:
            print(f"Uploaded {file_path} successfully.")
        else:
            print(f"Failed to upload {file_path}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error uploading data for file {file_path}: {e}")

    return fruit

def process_directory(directory):
    fruit_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            fruit = process_file(os.path.join(directory, filename))
            if fruit:
                fruit_list.append(fruit)
    return fruit_list

if __name__ == "__main__":
    directory = './supplier-data/descriptions'
    fruits = process_directory(directory)

    #test of dictionary
    for fruit in fruits:
        print(fruit)

