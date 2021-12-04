# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:55:21 2021

@author: PIYUSH KARMHE
"""
import cv2
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 

newpath = r'C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\img_dir' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
f=open("val2.txt","w+")
lable='3'

for i in range(20):
    #while lable!='0' or lable !='1':
    print("ONLY Labels 1 and 0 are allowed")
    lable=input("Give Lable : ")
    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        crop_img=img

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            crop_img=img[y:y+h, x:x+w]
        # Display
        cv2.imshow('img', img)

        #for capturing face only
        key = cv2.waitKey(1)
        if key == ord('s') or key == ord('S'): 
            #path="C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\img_dir\\"
            cv2.imwrite(filename='saved_img.jpg', img=crop_img)
            #cap.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            #cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 224X224 scale...")
            img_ = cv2.resize(gray,(224,224))
            print("Resized...")
            paths="C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\img_dir\\"
            img_resized = cv2.imwrite(os.path.join(paths,"saved_img-resized"+str(i)+".jpg"), img=img_)
            #img = cv2.imread('saved_img-resized"+str(i)+".jpg", cv2.IMREAD_ANYCOLOR)
            f.write("saved_img-resized"+str(i)+".jpg"+" "+lable+"\n")
            print("Image"+str(i+1)+" saved!")
        
            break
            # Stop if escape key is pressed
        elif key == ord('q') or key == ord('Q'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
f.close()        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
exec(open('initiator.py').read())
print("Successfully created ur database")