import pytesseract                              
from imutils.perspective import four_point_transform   
import matplotlib.pyplot as plt                     
import imutils
import cv2
import re
import requests
import numpy as np
from PIL import Image

class app:
    def __init__(self, url):
        self.originImg = cv2.imread(url)

    def findContours(self):
        cv2.imshow("original image", self.originImg)
        cv2.waitKey()

        image = self.originImg.copy()
        image = imutils.resize(image, width = 500)

        cv2.imshow("resize image", image)
        cv2.waitKey()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5, ), 0)
        edged = cv2.Canny(blurred, 75, 200)

        cv2.imshow("gray", gray)
        cv2.waitKey()
        cv2.imshow("blurred", blurred)
        cv2.waitKey()
        cv2.imshow("edged", edged)
        cv2.waitKey()

    def grouping(self):
    
    def detection(self):
    
    def recognition(self):
    
    def mergeResize(self):
    

        
url = 'img.jpg'
test = app(url)
test.findContours()