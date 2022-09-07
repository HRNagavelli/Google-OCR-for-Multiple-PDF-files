#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import libraries

from PIL import Image
import pytesseract
import re
import cv2
import sys
from tqdm import tqdm
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

for i in tqdm(range(10000)):

# Path of the pdf

    PDF_file = \
        r"C:\Users\hnagavelli\Documents\Py_Tessaract\10107677.pdf"

# Store all the pages of the PDF in a variable

pages = convert_from_path(PDF_file, 500)

# Counter to store images of each page of PDF to image

image_counter = 1

# Iterate through all the pages stored above

for page in pages:

    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    # ....
    # PDF page n -> page_n.jpg

    filename = 'page_' + str(image_counter) + '.jpg'

    # Save the image of the page in system

    page.save(filename, 'JPEG')

    # Increment the counter to update filename

    image_counter = image_counter + 1

# Variable to get count of total number of pages

filelimit = 1

# Creating a text file to write the output

outfile = r"C:\Users\hnagavelli\Documents\Py_Tessaract\output.txt"

# Open the file in append mode so that
# All contents of all images are added to the same file

f = open(outfile, 'a')

# Iterate from 1 to total number of pages

# for i in range(1, filelimit + 0):

    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg

filename = 'page_' + '1' + '.jpg'

    # Recognize the text as string in image using pytesserct

text = str(pytesseract.image_to_string(Image.open(filename)))
Date = re.findall('Order Number: [\d—-]+', text)
if Date:
    print (Date)

    # The recognized text is stored in variable text
    # Any string processing may be applied on text
    # Here, basic formatting has been done:
    # In many PDFs, at line ending, if a word can't
    # be written fully, a 'hyphen' is added.
    # The rest of the word is written in the next line
    # Eg: This is a sample text this word here GeeksF-
    # orGeeks is half on first line, remaining on next.
    # To remove this, we replace every '-\n' to ''.

text = text.replace('-\n', '')

    # Finally, write the processed text to the file.

f.write(text)

    # f.write(Date[0])

# Close the file after writing all the text.

f.close()



