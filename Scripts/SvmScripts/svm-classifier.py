import csv
import os
import sys
import cv2
from joblib import load
from keras.preprocessing import image
from pandas import np
from sklearn import svm


def driver():
    path = os.path.dirname(os.path.realpath(__file__))
    print("CWD: %s" % path)
    args = len(sys.argv) - 1
    if args < 1:
        raise Exception("Expected path")
    position = 1
    while args >= position:
        if not os.path.exists(sys.argv[position]):
            raise Exception("Expected existing directory...\n")
        position = position + 1
    print("Valid arguments. Applying masks...")
    patients = os.path.join(path, "patients")
    if not os.path.exists(patients):
        raise Exception("Expected existing directory in current folder: Patients\n")
    paths_target = os.path.join(path, "patients_m")
    if not os.path.exists(paths_target):
        os.mkdir(paths_target)
    paths_target = [os.path.join(paths_target, "Right"), os.path.join(paths_target, "Left")]
    for x in paths_target:
        if not os.path.exists(x):
            os.mkdir(x)
    apply_masks(patients, paths_target)
    compute_probabilites(path, os.path.join(path, "learn"))


def apply_masks(path, target):
    for file in os.listdir(path):
        root, ext = os.path.splitext(file)
        _end = [x + '\\' + file for x in target]
        [os.mkdir(x) for x in _end]
        _path = os.path.join(path, root)
        _path_ct = _path + '\\CT Scan'
        for _file in os.listdir(_path_ct):
            _current_path = os.path.join(_path_ct, _file)
            _path_masks = [_current_path.replace("CT Scan", "Masks\Mask1\OnlyLeftLung"),
                           _current_path.replace("CT Scan", "Masks\Mask1\OnlyRightLung")]
            for i in range(len(_path_masks)):
                __end = _end[i] + '\\' + _file
                os.mkdir(__end)
                for root, dirs, files in os.walk(_path_masks[i]):
                    for name in files:
                        mask = cv2.imread(os.path.join(root, name))
                        image = cv2.imread(os.path.join(_current_path, name))
                        mask = cv2.resize(mask, image.shape[1::-1])
                        dst1 = cv2.bitwise_and(image, mask)
                        cv2.imwrite(__end + '\\' + name, dst1)


def compute_probabilites(path, learning_path):
    print('Fitting...')
    svm_array = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
    if not os.path.exists(learning_path):
        raise Exception("Expected folder with models...")
    for i in range(2):
        for j in range(3):
            for k in range(3):
                svm_array[i][j][k] = svm.SVC(kernel='rbf', C=1.0)
    for i in range(2):
        for j in range(3):
            for k in range(3):
                svm_array[i][j][k] = load(os.path.join(learning_path, str(i) + str(j) + str(k) + '.joblib'))
    print("Models fitted")
    out = open('svm_results.csv', 'w', newline='')
    fields = ['Filename', 'LeftLungAffected', 'RightLungAffected', 'CavernsLeft', 'CavernsRight', 'PleurisyLeft',
              'PleurisyRight']
    if not os.path.exists(os.path.join(path, "patients_m")):
        raise Exception("Expected 'patients_m' folder...")
    else:
        _path = os.path.join(path, "patients_m")
        if os.path.exists(os.path.join(_path, "Left")) and os.path.exists(os.path.join(_path, "Right")):
            _path = [os.path.join(_path, "Left"), os.path.join(_path, "Right")]
        else:
            raise Exception("Expected subdirectories 'Left' and 'Right' in %s" % _path)
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    for file in os.listdir(_path[0]):
        location = [_path[0], _path[1]]
        test_data = [[[], [], []], [[], [], []]]
        for i in range(len(location)):
            for dirs in os.listdir(os.path.join(location[i], file)):
                region = 0 if dirs == 'FrontBack' else 1 if dirs == 'LeftRight' else 2
                _path = os.path.join(location[i], file, dirs)
                for _file in os.listdir(_path):
                    img = image.img_to_array(image.load_img(os.path.join(_path, _file), target_size=(32, 32)))
                    test_data[i][region].append(img)
        for i in range(2):
            for j in range(3):
                test_data[i][j] = np.array(test_data[i][j], dtype='float32') / 255.0
                m = test_data[i][j].shape[0]
                test_data[i][j] = test_data[i][j].reshape(m, -1)
        results = [[[[], [], []], [[], [], []], [[], [], []]], [[[], [], []], [[], [], []], [[], [], []]]]
        for i in range(2):
            for j in range(3):
                for k in range(3):
                    results[i][j][k] = svm_array[i][j][k].predict(test_data[i][j])
        final_result = [[[], [], []], [[], [], []]]
        for i in range(2):
            for j in range(3):
                final_result[i][j] = np.round(np.average([np.count_nonzero(arr == '1') / (
                        np.count_nonzero(arr == '1') + np.count_nonzero(arr == '0')) for arr in results[i][j]]), 2)
        writer.writerow(
            {'Filename': file, 'LeftLungAffected': final_result[0][0], 'RightLungAffected': final_result[1][0],
             'CavernsLeft': final_result[0][1], 'CavernsRight': final_result[1][1],
             'PleurisyLeft': final_result[0][2], 'PleurisyRight': final_result[1][2]})


if __name__ == "__main__":
    driver()
