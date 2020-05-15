import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import os  # dealing with directories
from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import csv

from PIL import Image


# https://pythonprogramming.net/convolutional-neural-network-kats-vs-dogs-machine-learning-tutorial/
# https://www.geeksforgeeks.org/
# ^^^^^^^^^^^^^^^^^^^^^^ bibliography


def def_labels_left_has_Tuberculosis(nume_pacient):
    with open('D:\\Git\\CT_Report.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nume_pacient:
                if row[1] == '0':
                    return [1, 0]  #n'are tbc
                if row[1] == '1':
                    return [0, 1]  # are tbc
                break


# def def_labels_left_has_Caverns(nume_pacient):
#     with open('D:\\Git\\CT_Report.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[0] == nume_pacient and row[1] == '1':
#                 if row[3] == '1':
#                     return [1, 0]  # are tbc
#                 if row[3] == '0':
#                     return [0, 1]  # nu are tbc
#                 break
#
#
# def def_labels_left_has_Pleurisy(nume_pacient):
#     with open('D:\\Git\\CT_Report.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[0] == nume_pacient and row[1] == '1':
#                 if row[5] == '1':
#                     return [1, 0]  # are tbc
#                 if row[5] == '0':
#                     return [0, 1]  # nu are tbc
#                 break


# getting the data
TRAIN_DIR = 'D:\\Git\\Processed-Images-Left'
TEST_DIR = 'D:\\Git\\test'
LR = 1e-3
IMG_SIZE = 64

MODEL_NAME = 'model(tuberculosis)-{}-{}.model'.format(LR,
                                                      '5conv-basic')  # just so we remember which saved model is which, sizes must match


# Now, we can build another function to fully process the training images and their labels into arrays:

def create_train_data_for_tbc():
    training_data = []
    count = 0
    subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])
        label = def_labels_left_has_Tuberculosis(sub[-3:])
        path = os.path.join(TRAIN_DIR, sub[-3:] + '\\FrontBack')
        for root, dirs, files in os.walk(path):
            # print("luam alt pacient")
            for name in files:
                # print("sunt aici la poza fiecarui pacient")
                count = count + 1
                img = cv2.imread(root + '\\' + name, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                training_data.append([np.array(img), np.array(label)])
        if int(sub[-3:]) == 177:
            break

    shuffle(training_data)
    print(count)
    return training_data


def create_test_data():
    test_data = []
    subfolders = [f.path for f in os.scandir(TEST_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])

        # label = def_labels_left(sub[-3:]) asta trebuie aici?
        testPath = os.path.join(TEST_DIR, sub[-3:] + '\\FrontBack')
        for root, dirs, files in os.walk(testPath):
            for name in files:
                img = cv2.imread(root + '\\' + name, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                test_data.append([np.array(img), name])
        if int(sub[-3:]) == 188:
            break
    return test_data


test_data = create_test_data()

train_data = create_train_data_for_tbc()

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression

import tensorflow as tf

tf.reset_default_graph()

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')
convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 128, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = conv_2d(convnet, 128, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 2, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

train = train_data[:-3000]
test = train_data[-3000:]

X = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=2, validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=2000, show_metric=True, run_id=MODEL_NAME)


with open('submission_file.csv', 'w') as f:
    f.write('pacient,label\n')

# with open('submission_file.csv', 'a') as f:
#     for data in tqdm(test_data):
#         img_num = data[1]
#         img_data = data[0]
#         data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
#         model_out = model.predict([data])[0]
#         f.write('{}, {}\n'.format(img_num, model_out[1]))


with open('submission_file.csv', 'a') as f:
    value = '177'
    avg = 0
    cont = 0
    valoare = 0
    for data in tqdm(test_data):
        img_num = data[1]

        if value in img_num:

            cont = cont + 1
            img_data = data[0]
            data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
            model_out = model.predict([data])[0]
            avg = avg + model_out[1]
        else:
            valoare = avg / cont
            f.write('{}, {}, {}, {}\n'.format(value, valoare, 'mediecav', 'medieple'))
            value1 = int(value)
            value1 = value1 + 1
            value = str(value1)

            avg = 0
            cont = 0
    valoare = avg / cont
    f.write('{}, {}, {}, {}\n'.format(value, valoare, 'mediecav', 'medieple'))