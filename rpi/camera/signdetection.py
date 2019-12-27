import cv2
import time
import imutils
import numpy as np

def process(image):

    img = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    stop_sign = cv2.CascadeClassifier.detectMultiScale(gray,1.02,10)

    cv2.rectangle(img,(x,y),(x+2,y+h),(255,0,0),2)
