#!/usr/bin/env python3

from PIL import Image
import os
import sys
import subprocess

output_directory = "/opt/icons/"
path = "/home/student-04-ba3f515e7e26/images/"

def get_images():
  # get a list of images name in /images
  images = [f for f in os.listdir(path)]
  return images

def process_images(images):
  for image in images:
  # Iterate through a list of images name
    if image != ".DS_Store":
    # Do not include any other file beside image file
    # Create image object and process them
      im = Image.open(os.path.join(path, image))
      im.rotate(90).resize((128,128)).convert("RGB").save(os.path.join(output_directory, image+".jpeg"))

if __name__ == "__main__":
  images = get_images()
  process_images(images)
