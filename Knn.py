import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


#path = ""
train_f = np.load("C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\dataset1.npz")
test_f= np.load("C:\\Users\\PIYUSH KARMHE\\Documents\\C++ codes\\dataset2.npz")
train_x = train_f['x']
train_y = train_f['y']
test_x = test_f['x']
test_y = test_f['y']
test_x=test_x.reshape(3,150528)
test_y=test_y.reshape(3,1)
train_x=train_x.reshape(20,150528)
train_y=train_y.reshape(20,)
knn = KNeighborsClassifier()
#train
knn.fit(train_x, train_y)
#make predictions # testing the model
print(knn.predict(train_x[0:]))
if knn.predict(train_x[18:19])==0:
    print("HI Piyush")
else:
    print("HI ANgelina")