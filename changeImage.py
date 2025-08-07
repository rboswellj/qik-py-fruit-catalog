#!/usr/bin/env python3

'''
Convert tiff files to smaller jpeg
        1. Size: Change image resolution from 3000x2000 to 600x400 pixel
        2. Format: Change image format from .TIFF to .JPEG
'''

import os
from PIL import Image

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.tiff'):
            process_image(os.path.join(directory, filename))

def process_image(image_path):
    with Image.open(image_path) as img:
        # Resize image to 600x400 pixels
        img = img.resize((600, 400))
        # Convert image to RGB mode if it is not already
        img = img.convert("RGB")
        # Convert image to JPEG format
        jpeg_image_path = image_path.replace('.tiff', '.jpeg')
        img.save(jpeg_image_path, 'JPEG')
        print(f"{image_path} output: {img.format}: {img.size}")

if __name__ == "__main__":
    directory = './supplier-data/images'  # Change this to your directory
    process_directory(directory)
    print("Image processing complete.")