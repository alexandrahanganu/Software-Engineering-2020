import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import os  # dealing with directories
from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import csv

from PIL import Image


def def_labels_right_has_Tuberculosis(nume_pacient):
    with open('D:\\Git\\CT_Report.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0] == nume_pacient:
                if row[2] == '1':
                    return [1,0]  # has does
                if row[2] == '0':
                    return [0,1]  # doesn't
                break


TRAIN_DIR='D:\\Git\\Processed-Images-Right'
IMG_SIZE=64


def create_train_data_for_tbc():
    training_data=[]
    count=0
    subfolders=[f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])
        label=def_labels_right_has_Tuberculosis(sub[-3:])
        path=os.path.join(TRAIN_DIR,sub[-3:]+'\\FrontBack')
        for root,dirs,files in os.walk(path):
            # print("luam alt pacient")
            for name in files:
                # print("sunt aici la poza fiecarui pacient")
                count=count+1
                img=cv2.imread(root+'\\'+name)
                # img = cv2.imread(root + '\\' + name)
                img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
                training_data.append([np.array(img),np.array(label)])

            path=os.path.join(TRAIN_DIR,sub[-3:]+'\\LeftRight')
            for root,dirs,files in os.walk(path):
                # print("luam alt pacient")
                for name in files:
                    # print("sunt aici la poza fiecarui pacient")
                    count=count+1
                    img=cv2.imread(root+'\\'+name)
                    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))

                    training_data.append([np.array(img),np.array(label)])

            path=os.path.join(TRAIN_DIR,sub[-3:]+'\\TopBottom')
            for root,dirs,files in os.walk(path):
                # print("luam alt pacient")
                for name in files:
                    # print("sunt aici la poza fiecarui pacient")
                    count=count+1
                    img=cv2.imread(root+'\\'+name)
                    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))

                    training_data.append([np.array(img),np.array(label)])

        if int(sub[-3:]) == 288:
            break

    shuffle(training_data)
    np.save('train_data_right_TBC.npy',training_data)
    return training_data


import os.path
from os import path

if path.exists('train_data_right_TBC.npy') is False: #if train_data doesn't exist / generate the file
    train_data=create_train_data_for_tbc()
else:
    train_data=np.load('train_data_right_TBC.npy',allow_pickle=True) #else just load it

train=train_data[:-3000]
test=train_data[-3000:]

easy=3

X=np.array([i[0] for i in train]).reshape(-1,IMG_SIZE,IMG_SIZE,easy)
Y=np.array([i[1] for i in train])

test_x=np.array([i[0] for i in test]).reshape(-1,IMG_SIZE,IMG_SIZE,easy)
test_y=np.array([i[1] for i in test])

from keras.models import Sequential
from keras.layers import Dense,Conv2D,Flatten

model=Sequential()
model.add(Conv2D(64,kernel_size=3,activation='relu',input_shape=(IMG_SIZE,IMG_SIZE,easy)))
model.add(Conv2D(32,kernel_size=3,activation='relu'))
model.add(Flatten())
model.add(Dense(2,activation='softmax'))

if path.exists('model_right_TBC.h5') is False: # check if model is already trained, if not train it
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    model.fit(X,Y,batch_size=200,validation_data=(test_x,test_y),epochs=3)
    model.save('model_right_TBC.h5')
else:
    model.load_weights('model_right_TBC.h5')

import sys
inputPath = sys.argv[1]
TEST_DIR = inputPath

IMG_SIZE=64
easy=3

# careful for the structure of the test file. i.e. : if ur test path is D:\\Git\\TestCTRs inside u should have CT Scan
# and Masks and it will take the path of CT Scan, then in CT Scan u should have FrontBack, LeftRight and TopBottom
# and inside these folders you should have your photos.
def create_test_data():
    test_data=[]
    count=0
    subfolders=[f.path for f in os.scandir(TEST_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])

        testPath=os.path.join(TEST_DIR,sub[-3:]+'\\CT Scan\\FrontBack')
        for root,dirs,files in os.walk(testPath):
            for name in files:
                count=count+1
                img=cv2.imread(root+'\\'+name)
                img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))

                test_data.append([np.array(img),name])

            testPath=os.path.join(TEST_DIR,sub[-3:]+'\\CT Scan\\LeftRight')
            for root,dirs,files in os.walk(testPath):
                for name in files:
                    img=cv2.imread(root+'\\'+name)
                    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))

                    test_data.append([np.array(img),name])

            testPath=os.path.join(TEST_DIR,sub[-3:]+'\\CT Scan\\TopBottom')
            for root,dirs,files in os.walk(testPath):
                for name in files:
                    img=cv2.imread(root+'\\'+name)
                    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))

                    test_data.append([np.array(img),name])

    return test_data


test_data=create_test_data()



with open('TBC_Results_Right.csv','w') as f:
    f.write('id, percentage\n')

with open('TBC_Results_Right.csv','a') as f:
    value=(test_data[1][1])[-12:-9]
    avg=0
    cont=0
    valoare=0
    for data in tqdm(test_data):
        img_num=data[1]

        if value in img_num:

            cont=cont+1
            img_data=data[0]
            data=img_data.reshape(-1,IMG_SIZE,IMG_SIZE,easy)
            model_out=model.predict([data])[0]
            avg=avg+model_out[0]
        else:
            valoare=avg / cont
            f.write('{}, {}\n'.format(value,valoare))
            value1=int(value)
            value1=value1+1
            value=str(value1)

            avg=0
            cont=0
    valoare=avg / cont
    f.write('{}, {}\n'.format(value,valoare))

