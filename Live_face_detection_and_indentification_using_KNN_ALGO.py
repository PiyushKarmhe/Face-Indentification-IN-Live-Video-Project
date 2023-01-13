# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:12:52 2021

@author: PIYUSH KARMHE
"""

import cv2
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from img_numpy_array import*
dirname = os.path.dirname(__file__)

image_dir=os.path.join(dirname, 'temp_dir')
label_file='val.txt'
classes=1000
input_height=224
input_width=224
input_chans=3
resize=True
normalize=False
one_hot=False
compress=True
output_file='dataset1.npz'

def pic():
    filename = os.path.join(dirname, './dataset_from_img.py')
    exec(open(filename).read())

def cam():
    filename = os.path.join(dirname, './dataset_from_cam.py')
    exec(open(filename).read())
    
filename = os.path.join(dirname, './temp_dir')
if not os.path.exists(filename):
    os.makedirs(filename)
path = os.path.join(dirname, './dataset1.npz')  
f=open("val.txt","w+")
f.write("saved_img-resized.jpg 0")  
f.close()
print("DO u have ur dataset?")
print("Total images : 20")
print("Size : 224X224")
print("Channel : 3")
print("Format : .npy or .pz")
ch=input("SO do u need to create a new Database?(Y Or N) : ")
if ch=='Y' or ch=='y':
    print("How u want to create ur Data base?")
    print("1.U have saved images but not of that specification?")
    print("2.U want take an image now?")
    choice=int(input("Give ANS : "))
    if choice==1:
        pic()
    else:
        cam()
else:
    path=input("Give Relative Path here : ")
    path = os.path.join(dirname, path) 
train_f = np.load(path)
train_x = train_f['x']
train_y = train_f['y']
train_x=train_x.reshape(20,150528)
train_y=train_y.reshape(20,)
knn = KNeighborsClassifier()
#train
knn.fit(train_x, train_y)
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
P1=input("Give name for person belonging to label 0 : ")
P2=input("Give name for person belonging to Label 1 : ")


while True:
    # Read the frame
    _, imgc = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    crop_img=imgc

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(imgc, (x, y), (x+w, y+h), (255, 0, 0), 2)
        crop_img=imgc[y:y+h, x:x+w]
        
    img_ = crop_img
    gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
    img_ = cv2.resize(img_,(224,224))
    path = os.path.join(dirname, './temp_dir')
    img_resized = cv2.imwrite(os.path.join(path,'./saved_img-resized.jpg'), img=img_)
    imgknn = images_to_npy(image_dir,label_file,classes,input_height,input_width,input_chans,resize,normalize,one_hot,compress,output_file)
    tempimg=imgknn[0]
    tempimg=tempimg.reshape(1,150528)
    x=knn.predict(tempimg)
    if x==0:
        for (x, y, w, h) in faces:
            cv2.putText(imgc, P1, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    elif x==1:
        for (x, y, w, h) in faces:
            cv2.putText(imgc, P2, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.imshow('img', imgc)
    key = cv2.waitKey(1)
    # Stop if escape key is pressed
    if key == ord('q') or key == ord('Q'):
        print("Turning off camera.")
        print("Program endeding.")
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
print("Camera Turned OFF")
print("Program Ended")