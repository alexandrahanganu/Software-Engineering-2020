import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from skimage.transform import resize
import warnings

def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"

        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        src = image_name
        shutil.move(src, outputlr)
    gc.collect()


def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        # move images to folder
        src = image_name
        shutil.move(src, outputfb)
    gc.collect()


def slice_tb(image_array, inputfile, outputtb, from_slice, to_slice):
    if to_slice > image_array.shape[2]:
        to_slice = image_array.shape[2]
    for current_slice in range(from_slice, to_slice):
        # alternate slices
        data = image_array[:, :, current_slice]
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        imageio.imwrite(image_name, data)
        # move images to folder
        src = image_name
        shutil.move(src, outputtb)
    gc.collect()


def main(argv):

    inputfileCT = "C:\\Users\\Dan\\Desktop\\testscans\\"
    outputfolder = "C:\\Users\\Dan\\Desktop\\TestScans\\" + "001"  # Output location

    file_name = "CTR_TRN_" + "001" + ".nii.gz"
    inputfileCT = inputfileCT + file_name

    outputlrCT = outputfolder + "\\CT Scan\\All\\LeftRight"
    outputfbCT = outputfolder + "\\CT Scan\\All\\FrontBack"
    outputtbCT = outputfolder + "\\CT Scan\\All\\TopBottom"


    image_arrayCT = nibabel.load(inputfileCT).get_fdata()
    image_arrayCT = image_arrayCT.astype(numpy.int16)

    # set destination folder
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

    aditionalDeleteCounter = 0
    for j in range(0, total_slicesLR):
        slice_lr(image_arrayCT, inputfileCT, outputlrCT, j, (j + 1))

    gc.collect()

    aditionalDeleteCounter = 0

    for j in range(0, 241):
        slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))

    for j in range(241,272):
        slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))

    for j in range(272, total_slicesFB):

        slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))

    for j in range(0, total_slicesTB):
        slice_tb(image_arrayCT, inputfileCT, outputtbCT, j, (j + 1))

    gc.collect()


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
