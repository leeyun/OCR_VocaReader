import pytesseract
from imutils.perspective import four_point_transform
import matplotlib.pyplot as plt
import imutils
import cv2
import re
import requests
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
a = Image.open('img.png')
result = pytesseract.image_to_string(a, lang = 'eng')
print(result)