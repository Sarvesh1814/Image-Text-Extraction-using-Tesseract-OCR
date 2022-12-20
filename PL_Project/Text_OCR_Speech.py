import re
import cv2
from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import pyttsx3


# Capturing the image from live video 
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
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "image{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()




# Processing the image 
filename = 'image0.png'
image = cv2.imread(filename)

 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lnovo\AppData\Local\Tesseract-OCR\tesseract.exe'
s=[]
ss=""
image1= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
results = pytesseract.image_to_data(image, output_type=Output.DICT)


for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]
    
    w = results["width"][i]
    h = results["height"][i]
    text = results["text"][i]

    conf = int(results["conf"][i])
    if True:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        s.append(text)
        spec=["@",',',"'",'"','/','&']
        if text.isalnum() or bool(re.match('^[a-zA-Z0-9]*$',"o")):
            ss = ss+" "+text
        else:
            pass
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image,text , (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

print(ss)

cv2.imshow("S",image)
cv2.waitKey(0) 
engine = pyttsx3.init()
engine.say(ss)
engine.runAndWait()
cv2.destroyAllWindows()


