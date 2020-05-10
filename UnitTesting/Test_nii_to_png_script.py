import unittest
import os
import time
from nii_to_png_script import niitopng,allZeros


processedScans="D:\\Software-Engineering-2020\\TrainCTRs"
inputScans="C:\\Scans"
class MyTestCase(unittest.TestCase):
    def test3DImageNotTakenIntoConsideration(self):
        self.assertEqual("Image is not a valid 3D Scan", niitopng(inputScans+"\\CTs\\",
                                                                  inputScans + "\\Masks1\\",
                                  inputScans+"\\Masks2\\", 620, 621))


    def testNumberOfImagesIsCorrect(self):

        numberOfFilesFB = len([name for name in os.listdir(processedScans+'\\001\\CT Scan\\FrontBack')])
        numberOfFilesLR = len([name for name in os.listdir(
            processedScans+'\\001\\CT Scan\\LeftRight')])
        numberOfFilesTB = len([name for name in os.listdir(
            processedScans+'\\001\\CT Scan\\TopBottom')])
        self.assertEqual(numberOfFilesFB, 68)
        self.assertEqual(numberOfFilesLR, 64)
        self.assertEqual(numberOfFilesTB, 23)

    def testAllZeros(self):
        listOfLists = [[]]
        listOfLists.append([1, 2, 3])
        listOfLists.append([1, 1, 1])
        self.assertEqual(False, allZeros(listOfLists))
        listOfListsZero = [[]]
        listOfListsZero.append([0, 0, 0])
        listOfListsZero.append([0, 0, 0])
        self.assertEqual(True, allZeros(listOfListsZero))

    def testFileExists(self):
        self.assertEqual("At least one of the files does not exist",
            niitopng(inputScans+"\\CTs\\",
                     inputScans+"\\Masks1\\",
                     inputScans + "\\Masks2\\", 300, 320))

    def testSameNumberOfFiles(self):

        folderctFB = len(os.listdir(
            processedScans+"\\001\\CT Scan\\FrontBack"))
        folderctLR = len(os.listdir(
            processedScans+"\\001\\CT Scan\\LeftRight"))
        folderctTB = len(os.listdir(
            processedScans+"\\001\\CT Scan\\TopBottom"))

        folderM1FB = len(os.listdir(
            processedScans+"\\001\\Masks\\Mask1\\FrontBack"))
        folderM1LR = len(os.listdir(
            processedScans+"\\001\\Masks\\Mask1\\LeftRight"))
        folderM1TB = len(os.listdir(
            processedScans + "\\001\\Masks\\Mask1\\TopBottom"))

        folderM2FB = len(os.listdir(
            processedScans+"\\001\\Masks\\Mask2\\FrontBack"))
        folderM2LR = len(os.listdir(
            processedScans+"\\001\\Masks\\Mask2\\LeftRight"))
        folderM2TB = len(os.listdir(
            processedScans+"\\001\\Masks\\Mask2\\TopBottom"))

        self.assertEqual(folderctFB,folderM1FB)
        self.assertEqual(folderctFB,folderM2FB)

        self.assertEqual(folderctLR,folderM1LR)
        self.assertEqual(folderctLR,folderM2LR)

        self.assertEqual(folderctTB,folderM1TB)
        self.assertEqual(folderctTB,folderM2TB)

    def testFileNotEmpty(self):
        self.assertEqual("Empty file detected", niitopng(inputScans+"\\CTs\\",inputScans+"\\Masks1\\",
                                  inputScans+"\\Masks2\\", 622, 623))
    def test_suprascriere(self):
        outputfolder =inputScans+"\\Processed\\079"
        if os.path.exists(outputfolder):
            old_time=time.ctime(os.path.getctime(outputfolder))
            niitopng(inputScans+"\\CTs\\", inputScans+"\\Masks1\\",inputScans+"\\Masks2\\", 79, 80)
            new_time=time.ctime(os.path.getctime(outputfolder))
            self.assertTrue(old_time != new_time)
        else:
            niitopng(inputScans+"\\CTs\\", inputScans+"\\Masks1\\",inputScans+"\\Masks2\\", 79, 80)
            new_time = time.ctime(os.path.getmtime(outputfolder))
            self.assertTrue(new_time != 0)
    def test_existentaFelii(self):
        outputfolder = inputScans+"\\Processed\\079"
        masksfolder = outputfolder + "\\Masks"
        for subdir, dirs, files in os.walk(masksfolder):
            for file in files:
                filepath = subdir + os.sep + file
                ct_file = filepath.replace("Masks\\Mask1\\OnlyLeftLung", "CT Scan")
                ct_file = ct_file.replace("Masks\\Mask1\\OnlyRightLung", "CT Scan")
                ct_file = ct_file.replace("Masks\\Mask1", "CT Scan")
                ct_file = ct_file.replace("Masks\\Mask2", "CT Scan")
                self.assertTrue(os.path.exists(ct_file))

if __name__ == '__main__':
    unittest.main()
