# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:27:40 2021

@author: PIYUSH KARMHE
"""
import cv2
import os
dirname = os.path.dirname(__file__)

# Load the cascade
filename = os.path.join(dirname, './haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(filename)
print("First copy all the images into us folder which has all the python files")

filename = os.path.join(dirname, './img_dir')
if not os.path.exists(filename):
    os.makedirs(filename)
f=open("val2.txt","w+")
# Read the input image
lable='3'
for i in range(20):
    img_name=input("Give Image Name : ")
    print("ONLY Labels 1 and 0 are allowed")
    lable=input("Give Lable : ")
        
    img = cv2.imread(img_name)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crop_img=img[y:y+h, x:x+w]
    # Display the output
    cv2.imshow('img', crop_img)
    #for capturing face only
    cv2.imwrite(filename='saved_img.jpg', img=crop_img)
    img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
    img_new = cv2.imshow("Captured Image", img_new)
    print("Processing image...")
    img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
    print("Converting RGB image to grayscale...")
    print("img_ shape : ",img_.shape)
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    print("Converted RGB image to grayscale...")
    print("Resizing image to 224X244 scale...")
    print("Gray shape : ",gray.shape)
    img_ = cv2.resize(gray,(224,224))
    print("Resized...")
    path="C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\img_dir\\"
    filename = os.path.join(dirname, './img_dir')
    img_resized = cv2.imwrite(os.path.join(filename,"./saved_img-resized"+str(i)+".jpg"), img=img_)
    img = cv2.imread("saved_img-resized"+str(i)+".jpg", cv2.IMREAD_ANYCOLOR)
    f.write("saved_img-resized"+str(i)+".jpg"+" "+lable+"\n")
    print("Image"+str(i+1)+" saved!")
    cv2.waitKey()
f.close()
exec(open('initiator.py').read())
print("Successfully created ur database")