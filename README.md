# Face-Indentification-IN-Live-Video-Project
Live Face Identification Project Using KNN Algorithm
It uses KNN Algorithm
I ahve provided sample datasets
dataset1.npz
dataset2.npz
Working
I loades dataset1.npz into model for it's trainig
then opens webcam
analysis each frame
indentifies face in it
crops it
processes it and makes numpy array from it
then it makes predections ussing Knn model to identify the person
IF identified then his/her name is displayed on the live cam.[readme.txt](https://github.com/PiyushKarmhe/Face-Indentification-IN-Live-Video-Project/files/7650764/readme.txt)
[readme.txt](https://github.com/PiyushKarmhe/Face-Indentification-IN-Live-Video-Project/files/7650767/readme.txt)
Live_face_detection_and_indentification_using_KNN_ALGO**** is the driver file
just change the values of path variables the last part od that string need be the same like database.npz or img_dir needs to remain there only the path before that need to be changed.
while using the already present images to create a database make sure to copy those in the same folder as of all the other files.
Thank you.
Paths to be changed before using:-
File:- Live_face_detection_and_indentification_using_KNN_ALGO.py
L[40]: newpath = r'C:\\Users\\......\\temp_dir'
L[43]: path="C:\\Users\\.....\\dataset.npz"
L[102]: path="C:\\Users\\......\\temp_dir\\"
File:- dataset_from_cam.py
L[17]: newpath = r'C:\\Users\\.....\\img_dir'
L[64]: paths="C:\\Users\\.....\\img_dir\\"
File:- dataset_from_img.py
L[14]: newpath = r'C:\\Users\\.....\\img_dir'
L[53]: path="C:\\Users\\.....\\img_dir\\"
