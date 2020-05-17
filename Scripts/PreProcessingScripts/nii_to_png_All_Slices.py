import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from skimage.transform import resize
import warnings
from time import time

def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"

        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputlr + "\\" + image_name, data)


def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputfb + "\\" + image_name, data)


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
    sys.setrecursionlimit(1500)
    start = time()

    inputfileCT = argv[0]

    outputfolder = "C:\\Users\\denis\\Desktop\\TestScans\\" + os.path.basename(argv[0]).split(".",1)[0]  # Output location

    filenameCT = os.path.basename(argv[0]).split(".",1)[0]

    outputlrCT = outputfolder + "\\CT Scan\\LeftRight"
    outputfbCT = outputfolder + "\\CT Scan\\FrontBack"
    outputtbCT = outputfolder + "\\CT Scan\\TopBottom"

    image_arrayCT = nibabel.load(inputfileCT).get_fdata()
    image_arrayCT = image_arrayCT.astype(numpy.int16)

    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
    else:
        shutil.rmtree(outputfolder)
        os.makedirs(outputfolder)

    os.makedirs(outputlrCT)
    os.makedirs(outputfbCT)
    os.makedirs(outputtbCT)

    total_slicesLR = image_arrayCT.shape[0]
    total_slicesFB = image_arrayCT.shape[1]
    total_slicesTB = image_arrayCT.shape[2]

    for j in range(0, total_slicesLR):
        slice_lr(image_arrayCT, filenameCT, outputlrCT, j, (j + 1))
    gc.collect()

    for j in range(0, total_slicesFB):
        slice_fb(image_arrayCT, filenameCT, outputfbCT, j, (j + 1))

    for j in range(0, total_slicesTB):
        slice_tb(image_arrayCT, filenameCT, outputtbCT, j, (j + 1))

    end = time()
    print('\n\n\n', (end - start), "sec")


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
