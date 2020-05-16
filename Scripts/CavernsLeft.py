import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import os  # dealing with directories
from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import csv

from PIL import Image

def def_labels_left_has_caverns(nume_pacient):
    with open('D:\\Git\\CT_Report.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nume_pacient:
                if row[4] == '1':
                    return [1, 0]  # has caverns
                if row[4] == '0':
                    return [0, 1]  # doesn't have caverns
                break


# getting the data
import sys
inputPath = sys.argv[1]
TRAIN_DIR = 'D:\\Git\\Processed-Images-Left'
TEST_DIR = inputPath
IMG_SIZE = 64

def create_train_data_for_tbc():
    training_data = []
    count = 0
    subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])
        label = def_labels_left_has_caverns(sub[-3:])
        path = os.path.join(TRAIN_DIR, sub[-3:] + '\\FrontBack')
        for root, dirs, files in os.walk(path):
            # print("luam alt pacient")
            for name in files:
                # print("sunt aici la poza fiecarui pacient")
                count = count + 1
                img = cv2.imread(root + '\\' + name)
                #img = cv2.imread(root + '\\' + name)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                training_data.append([np.array(img), np.array(label)])

            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\LeftRight')
            for root, dirs, files in os.walk(path):
                # print("luam alt pacient")
                for name in files:
                    # print("sunt aici la poza fiecarui pacient")
                    count = count + 1
                    img = cv2.imread(root + '\\' + name)
                    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                    training_data.append([np.array(img), np.array(label)])

            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\TopBottom')
            for root, dirs, files in os.walk(path):
                # print("luam alt pacient")
                for name in files:
                    # print("sunt aici la poza fiecarui pacient")
                    count = count + 1
                    img = cv2.imread(root + '\\' + name)
                    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                    training_data.append([np.array(img), np.array(label)])

        if int(sub[-3:]) == 100:
            break

    shuffle(training_data)
    # np.save('train_data.npy', training_data)
    print(count)
    return training_data


def create_test_data():
    test_data = []
    count = 0
    subfolders = [f.path for f in os.scandir(TEST_DIR) if f.is_dir()]
    for sub in subfolders:
        print(sub[-3:])

        testPath = os.path.join(TEST_DIR, sub[-3:] + '\\FrontBack')
        for root, dirs, files in os.walk(testPath):
            for name in files:
                count = count+1
                img = cv2.imread(root + '\\' + name)
                #img = cv2.imread(root + '\\' + name)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                test_data.append([np.array(img), name])

            testPath = os.path.join(TEST_DIR, sub[-3:] + '\\LeftRight')
            for root, dirs, files in os.walk(testPath):
                for name in files:
                    img = cv2.imread(root + '\\' + name)
                    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                    test_data.append([np.array(img), name])

            testPath = os.path.join(TEST_DIR, sub[-3:] + '\\TopBottom')
            for root, dirs, files in os.walk(testPath):
                for name in files:
                    img = cv2.imread(root + '\\' + name)
                    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

                    test_data.append([np.array(img), name])

        if int(sub[-3:]) == 188:
            break

    # shuffle(test_data)
    # np.save('test_data.npy', test_data)
    return test_data


#reshape data to fit model

train_data = create_train_data_for_tbc()
test_data = create_test_data()

train = train_data[:-500]
test = train_data[-500:]

easy = 3

X = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE, easy)
Y = np.array([i[1] for i in train])

test_x = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, easy)
test_y = np.array([i[1] for i in test])


from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
#create model
model = Sequential()
#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, easy)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


model.fit(X, Y, batch_size = 200, validation_data=(test_x, test_y), epochs=3)


with open('Caverns_Results_Left.csv', 'w') as f:
    f.write('id,label\n')

with open('Caverns_Results_Left.csv', 'a') as f:
    value = '178'
    avg = 0
    cont = 0
    valoare = 0
    for data in tqdm(test_data):
        img_num = data[1]

        if value in img_num:

            cont = cont + 1
            img_data = data[0]
            data = img_data.reshape(-1, IMG_SIZE, IMG_SIZE, easy)
            model_out = model.predict([data])[0]
            avg = avg + model_out[0]
        else:
            valoare = avg / cont
            f.write('{}, {}\n'.format(value, valoare))
            value1 = int(value)
            value1 = value1 + 1
            value = str(value1)

            avg = 0
            cont = 0
    valoare = avg / cont
    f.write('{}, {}\n'.format(value, valoare))