import cv2
import os
from PIL import Image
import math
import random
import sys
file = str(random.randint(1000000,9999999))
path = "/var/www/html/compressed/"+file+".jpg"
cascPath = "haarcascade_frontalface_default.xml"
imagePath = sys.argv[1];
size = os.path.getsize(imagePath)
size /= 1024
roundsize = round(size,3)
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.6,
    minNeighbors=4,
    minSize=(4, 4),
)
s = int (format(len(faces)));

if (s > 0 ):
   # print("Select Exam type :")
   # print("1)JEE")
   # print("2)VITEEE")
   # print("3)GATE")
    Exam_type="JEE"
    if Exam_type=="JEE":
        if 10 < roundsize < 200:
            print("The submitted file is a photograph and valid for JEE exam ")
        else:
            print("File size is to small or to large mantain the size under 10Kb and over 200Kb ")
            print("Uploaded File Size: ", roundsize)
            foo = Image.open(imagePath)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1100)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save(path, quality=95)
            print("File Compressed and Submitted succesfully")
    elif Exam_type=="VITEEE":
        if 10 < roundsize < 200:
            print("The submitted file is a photograph and valid for VITEEE exam")
        else:
            print("File size is to small or to large mantain the size under 10Kb and over 200Kb " )
            print("Uploaded File Size: ", roundsize)
            foo = Image.open(imagePath)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1100)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save(path, quality=95)
            print("File Compressed and Submitted succesfully")

    elif Exam_type=="GATE":
         if 10 < roundsize < 200:
            print("The submitted file is a photograph and valid for GATE exam")
         else:
            print("File size is to small or to large mantain the size under 10Kb and over 200Kb ")
            print("Uploaded File Size: ", roundsize)
            foo = Image.open(imagePath)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1100)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save(path, quality=95)
            print("File Compressed and Submitted succesfully")
    else:
        print("Enter Valid Exam name")
else:
    print("No it is not a photograph. Please choose right image.")

