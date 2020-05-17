import sys
import nibabel
import numpy
import os
import shutil
import imageio
import gc
from concurrent.futures import ThreadPoolExecutor, wait
from skimage.transform import resize
import warnings


def slice_lr(image_array, inputfile, outputlr, from_slice, to_slice):
    if to_slice > image_array.shape[0]:
        to_slice = image_array.shape[0]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[current_slice, :, :])
        image_name = inputfile + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        #data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputlr + "\\" + image_name, data)


def slice_fb(image_array, inputfile, outputfb, from_slice, to_slice):
    if to_slice > image_array.shape[1]:
        to_slice = image_array.shape[1]
    for current_slice in range(from_slice, to_slice):
        data = numpy.rot90(image_array[:, current_slice, :])
        image_name = inputfile + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        #data = data.astype(numpy.float32)
        data = resize(data, (512, 512))
        imageio.imwrite(outputfb + "\\" + image_name, data)


def slice_tb(image_array, inputfile, outputtb, from_slice, to_slice):
    if to_slice > image_array.shape[2]:
        to_slice = image_array.shape[2]
    for current_slice in range(from_slice, to_slice):
        data = image_array[:, :, current_slice]
        image_name = inputfile + "_z" + "{:0>3}".format(str(current_slice + 1)) + ".png"
        #data = data.astype(numpy.float32)
        imageio.imwrite(outputtb + "\\" + image_name, data)
    gc.collect()


def main(argv):
    inputfileCT = argv[0]

    outputfolder = "C:\\xampp\\htdocs\\ProcessedPatients\\" + os.path.basename(argv[0]).split(".", 1)[0]  # Output location

    filenameCT = os.path.basename(argv[0]).split(".", 1)[0]

    outputlrCT = outputfolder + "\\CT Scan\\All\\LeftRight"
    outputfbCT = outputfolder + "\\CT Scan\\All\\FrontBack"
    outputtbCT = outputfolder + "\\CT Scan\\All\\TopBottom"

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

    threads = 4

    executor = ThreadPoolExecutor(threads)
    futures = []
    lr = [65, 435]  # [ min , max ] values for left right
    fb = [100, 380]  # [ min , max ] values for front back
    tb = [15, 100]  # [ min , max ] values for top bottom
    for i in range(0, threads):
        val = int(lr[1] / threads)
        from_slice = i * val + lr[0]
        to_slice = (i + 1) * val + lr[0]
        if to_slice > lr[1]:
            to_slice = lr[1]
        futures.append(executor.submit(slice_lr, image_arrayCT, filenameCT, outputlrCT, from_slice, to_slice))
    for i in range(0, threads):
        val = int(fb[1] / threads)
        from_slice = i * val + fb[0]
        to_slice = (i + 1) * val + fb[0]
        if to_slice > fb[1]:
            to_slice = fb[1]
        futures.append(executor.submit(slice_fb, image_arrayCT, filenameCT, outputfbCT, from_slice, to_slice))
    for i in range(0, threads):
        val = int(tb[1] / threads)
        from_slice = i * val + tb[0]
        to_slice = (i + 1) * val + tb[0]
        if to_slice > tb[1]:
            to_slice = tb[1]
        futures.append(executor.submit(slice_tb, image_arrayCT, filenameCT, outputtbCT, from_slice, to_slice))

    wait(futures)


# call the function to start the program
if __name__ == "__main__":
    main(sys.argv[1:])
