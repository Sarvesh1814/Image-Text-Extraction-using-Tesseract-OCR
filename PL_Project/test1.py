import re
import cv2
from PIL import Image
import easyocr
import numpy as np

import pyttsx3


#Capturing the image from live video 
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        img_name = "image0.png"
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "image{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


reader = easyocr.Reader(['en'])
results = reader.readtext("image0.png")

text=''
for i in range(len(results)):
    text=text+" "+results[i][1]
print(text)

image = cv2.imread("image0.png")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()




