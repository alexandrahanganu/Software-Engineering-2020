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


def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile[:-7] + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(image_name, data)
        # move images to folder
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


def niitopng(inputDirCT, inputDirM1, inputDirM2, from_image, to_image):
    number_of_threads = 4  # Number of threads used
    toScan = []

    for i in range(from_image, to_image):
        inputfileM1 = inputDirM1  # Scans location
        inputfileM2 = inputDirM2
        inputfileCT = inputDirCT
        # Scan number
        j = i
        if i < 10:
            j = "00" + str(i)
        elif i < 100:
            j = "0" + str(i)
        elif i < 1000:
            j = str(i)
        outputfolder = "C:\\Scans\\Processed\\" + j  # Output location

        file_name = "CTR_TRN_" + str(j) + ".nii.gz"

        outputlrM1 = outputfolder + "\\Masks\\Mask1\\LeftRight"
        outputfbM1 = outputfolder + "\\Masks\\Mask1\\FrontBack"
        outputtbM1 = outputfolder + "\\Masks\\Mask1\\TopBottom"

        outputlrM2 = outputfolder + "\\Masks\\Mask2\\LeftRight"
        outputfbM2 = outputfolder + "\\Masks\\Mask2\\FrontBack"
        outputtbM2 = outputfolder + "\\Masks\\Mask2\\TopBottom"

        outputlrCT = outputfolder + "\\CT Scan\\LeftRight"
        outputfbCT = outputfolder + "\\CT Scan\\FrontBack"
        outputtbCT = outputfolder + "\\CT Scan\\TopBottom"
        try:

            inputfileM1 = inputfileM1 + file_name
            if os.path.exists(inputfileM1) and os.stat(inputfileM1).st_size == 0:
                return "Empty file detected"

            inputfileM2 = inputfileM2 + file_name

            if os.path.exists(inputfileM2) and os.stat(inputfileM2).st_size == 0:
                return "Empty file detected"

            inputfileCT = inputfileCT + file_name

            if os.path.exists(inputfileCT) and os.stat(inputfileCT).st_size == 0:
                return "Empty file detected"
            image_arrayM1 = nibabel.load(inputfileM1).get_fdata()
            # image_arrayM1 = image_arrayM1.astype(numpy.int16)

            image_arrayM2 = nibabel.load(inputfileM2).get_fdata()
            # image_arrayM2 = image_arrayM2.astype(numpy.int16)

            image_arrayCT = nibabel.load(inputfileCT).get_fdata()
            # image_arrayCT = image_arrayCT.astype(numpy.int16)



        except FileNotFoundError:
            return "At least one of the files does not exist"
        except Exception:
            return "Image is not a valid 3D Scan"
        if len(image_arrayM1.shape) == 3:
            # set destination folder
            if not os.path.exists(outputfolder):
                os.makedirs(outputfolder)
                print("Created output directory: " + outputfolder)
            else:
                shutil.rmtree(outputfolder)
                os.makedirs(outputfolder)

            os.makedirs(outputlrM1)
            os.makedirs(outputfbM1)
            os.makedirs(outputtbM1)

            os.makedirs(outputlrM2)
            os.makedirs(outputfbM2)
            os.makedirs(outputtbM2)

            os.makedirs(outputlrCT)
            os.makedirs(outputfbCT)
            os.makedirs(outputtbCT)

            print("Processing " + file_name + "...")

            total_slicesLR = image_arrayM1.shape[0]
            total_slicesFB = image_arrayM1.shape[1]
            total_slicesTB = image_arrayM1.shape[2]

            futures = []
            for j in range(0, total_slicesLR):
                if j % 4 == 0 and not (allZeros(image_arrayM1[j, :, :])):
                    slice_lr(image_arrayM1, inputfileM1, outputlrM1, j, (j + 1))
                    slice_lr(image_arrayM2, inputfileM2, outputlrM2, j, (j + 1))
                    slice_lr(image_arrayCT, inputfileCT, outputlrCT, j, (j + 1))
            gc.collect()

            for j in range(0, total_slicesFB):
                if j % 4 == 0 and not (allZeros(image_arrayM1[:, j, :])):
                    slice_fb(image_arrayM1, inputfileM1, outputfbM1, j, (j + 1))
                    slice_fb(image_arrayM2, inputfileM2, outputfbM2, j, (j + 1))
                    slice_fb(image_arrayCT, inputfileCT, outputfbCT, j, (j + 1))
            gc.collect()
            for j in range(0, total_slicesTB):
                if j % 4 == 0 and not (allZeros(image_arrayM1[:, :, j])):
                    slice_tb(image_arrayM1, inputfileM1, outputtbM1, j, (j + 1))
                    slice_tb(image_arrayM2, inputfileM2, outputtbM2, j, (j + 1))
                    slice_tb(image_arrayCT, inputfileCT, outputtbCT, j, (j + 1))
            gc.collect()
        else:
            return "Image should be 3D"
    print("Succeded")


inputScans = "C:\\Scans"
if __name__ == "__main__":
    niitopng(inputScans + "\\CTs\\", inputScans + "\\Masks1\\", inputScans + "\\Masks2\\", 79, 80)
