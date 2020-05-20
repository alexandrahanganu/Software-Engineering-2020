import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from skimage.transform import resize

def allZeros(list):
    for elem in list:
        for number in elem:
            if number != 0:
                return False
    return True

def deleteLastN(folder, n):
    listOfFiles = os.listdir(folder)
    listOfFiles.sort(reverse=True)
    for i in range(0,n):
        os.remove(folder + "\\" + listOfFiles[i])

def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"

        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputlr + "\\" + image_name, data)

    gc.collect()


def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputfb + "\\" + image_name, data)

    gc.collect()


def slice_tb(image_array, inputfile, outputtb, from_slice, to_slice):
    if to_slice > image_array.shape[2]:
        to_slice = image_array.shape[2]
    for current_slice in range(from_slice, to_slice):
        # alternate slices
        data = image_array[:, :, current_slice]
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        imageio.imwrite(outputtb + "\\" + image_name, data)
    gc.collect()


def main(argv):

    inputfileM1 = argv[1]
    inputfileCT = argv[0]

    outputfolder = "C:\\xampp\\htdocs\\Software-Engineering2020\\Algorithm Input" + os.path.basename(argv[0]).split(".",1)[0]  # Output location

    filenameM1 = os.path.basename(argv[1]).split(".",1)[0]
    filenameCT = os.path.basename(argv[0]).split(".",1)[0]

    outputlrM1 = outputfolder + "\\Masks\\Mask1\\LeftRight"
    outputfbM1 = outputfolder + "\\Masks\\Mask1\\FrontBack"
    outputtbM1 = outputfolder + "\\Masks\\Mask1\\TopBottom"

    outputlrCT = outputfolder + "\\CT Scan\\LeftRight"
    outputfbCT = outputfolder + "\\CT Scan\\FrontBack"
    outputtbCT = outputfolder + "\\CT Scan\\TopBottom"

    image_arrayM1 = nibabel.load(inputfileM1).get_fdata()
    image_arrayM1 = image_arrayM1.astype(numpy.int16)

    image_arrayCT = nibabel.load(inputfileCT).get_fdata()
    image_arrayCT = image_arrayCT.astype(numpy.int16)

    if len(image_arrayM1.shape) == 3:
        # set destination folder
        if not os.path.exists(outputfolder):
            os.makedirs(outputfolder)

        else:
            shutil.rmtree(outputfolder)
            os.makedirs(outputfolder)

        os.makedirs(outputlrM1)
        os.makedirs(outputfbM1)
        os.makedirs(outputtbM1)

        os.makedirs(outputlrCT)
        os.makedirs(outputfbCT)
        os.makedirs(outputtbCT)

        total_slicesLR = image_arrayM1.shape[0]
        total_slicesFB = image_arrayM1.shape[1]
        total_slicesTB = image_arrayM1.shape[2]

        aditionalDeleteCounter = 0
        for j in range(0, total_slicesLR):
            if j % 4 == 0 and (j < 225 or j>275) and not(allZeros(image_arrayM1[j, :, :])):
                if aditionalDeleteCounter > 4:
                    slice_lr(image_arrayM1, filenameM1, outputlrM1, j, (j + 1))
                    slice_lr(image_arrayCT, filenameCT, outputlrCT, j, (j + 1))
                else:
                    aditionalDeleteCounter += 1

        gc.collect()
        deleteLastN(outputlrCT, 5)
        deleteLastN(outputlrM1, 5)

        aditionalDeleteCounter = 0

        for j in range(0, 241):
            if j % 4 == 0 and not(allZeros(image_arrayM1[:, j, :])):
                if aditionalDeleteCounter > 10:
                    slice_fb(image_arrayM1, filenameM1, outputfbM1, j, (j + 1))
                    slice_fb(image_arrayCT, filenameCT, outputfbCT, j, (j + 1))
                else:
                    aditionalDeleteCounter += 1
        for j in range(241,272):
            slice_fb(image_arrayM1, filenameM1, outputfbM1, j, (j + 1))
            slice_fb(image_arrayCT, filenameCT, outputfbCT, j, (j + 1))

        for j in range(272, total_slicesFB):
            if j % 4 == 0 and not(allZeros(image_arrayM1[:, j, :])):
                slice_fb(image_arrayM1, filenameM1, outputfbM1, j, (j + 1))
                slice_fb(image_arrayCT, filenameCT, outputfbCT, j, (j + 1))

        deleteLastN(outputfbCT,10)
        deleteLastN(outputfbM1,10)
        aditionalDeleteCounter = 0

        for j in range(0, total_slicesTB):
            if j % 4 == 0 and not(allZeros(image_arrayM1[:, :, j])):
                if aditionalDeleteCounter > 4:
                    slice_tb(image_arrayM1, filenameM1, outputtbM1, j, (j + 1))
                    slice_tb(image_arrayCT, filenameCT, outputtbCT, j, (j + 1))
                else:
                    aditionalDeleteCounter += 1
        deleteLastN(outputtbCT, 4)
        deleteLastN(outputtbM1, 4)

        gc.collect()


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
