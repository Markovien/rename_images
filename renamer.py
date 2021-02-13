# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:14:07 2021

@author: @Markovien
"""
import os, shutil
from PIL import Image

INPUT_FOLDER = "absolute path to images to rename"
OUTPUT_FOLDER = "absolute path to renamed images"

def prepare_folders():
    """
    return: void
        Creates necessary folders
    """

    for folder in [
        INPUT_FOLDER, OUTPUT_FOLDER
    ]:
        if not os.path.exists(folder):
            os.makedirs(folder)

def find_images(folder):
    """
    param: str
        Path to folder to search
    return: generator of str
        List of images in folder
    """

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            try:
                Image.open(full_path)  
                yield file
            except:
                pass

def rename_images():
    images = list(find_images(INPUT_FOLDER))
    i = 1
    for img in images:
        #output_path = OUTPUT_FOLDER + img.split(".")[0] + ".jpg"
        input_path = os.path.join(INPUT_FOLDER, img)
        output_path = OUTPUT_FOLDER + 'image_' + str(i) + '.jpg'
        
        with open(input_path, 'rb') as file_in:
            with open(output_path, 'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)
        
        i+=1

prepare_folders()
rename_images()
