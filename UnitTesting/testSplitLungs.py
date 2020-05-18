from splitLungs import isFinalDir
import os
import unittest
from splitLungs import separateLungs
import splitLungs


class MyTestCase(unittest.TestCase):
    def test_equalNumberOfOutputFilesFrontBackLeftLung(self):
        onlyleftlungfrontback = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"))
        frontback = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack"))
        self.assertEqual(onlyleftlungfrontback, frontback)

    def test_equalNumberOfOutputFilesTopBottomLeftLung(self):
        onlyleftlungtopbottom = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom"))
        topbottom = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom"))
        self.assertEqual(onlyleftlungtopbottom, topbottom)

    def test_equalNumberOfOutputFilesFrontBackrightLung(self):
        onlyrightlungfrontback = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"))
        frontback = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack"))
        self.assertEqual(onlyrightlungfrontback, frontback)

    def test_equalNumberOfOutputFilesTopBottomLeftLung(self):
        onlyrightlungtopbottom = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom"))
        topbottom = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom"))
        self.assertEqual(onlyrightlungtopbottom, topbottom)

    def test_isFinalDirFalse(self):
        self.assertFalse(isFinalDir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TestCTRs\\001"))

    def test_ifFinalDirTrue(self):
        self.assertTrue(isFinalDir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\CT Scan\\FrontBack"))

    def test_equalNumberOfFiles(self):
        onlyleftlung = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung"))
        onlyrightlung = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung"))
        self.assertEqual(onlyleftlung, onlyrightlung)

    def test_allInputFilesArePngFrontBack(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack"))
        self.assertTrue(first, nr1)

    def test_allInputFilesArePngTopBottom(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom"))
        self.assertTrue(first, nr1)

    def test_allInputFilesArePngLeftRight(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\LeftRight"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyLeftLungFrontBack(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyLeftLungLeftRight(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyLeftLungTopBottom(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyRightLungFrontBack(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyRightLungTopBottom(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom"))
        self.assertTrue(first, nr1)

    def test_allOutputFilesArePngOnlyRightLungLeftRight(self):
        first = 0
        for root, dirs, files in os.walk(
                "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight"):
            for file in files:
                if file.endswith(".png"):
                    first = first + 1
        nr1 = len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight"))
        self.assertTrue(first, nr1)

    def test_inputDirectoryExistTopBottom(self):
        self.assertTrue(os.path.isdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom"))

    def test_inputDirectoryExistLeftRight(self):
        self.assertTrue(os.path.isdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\LeftRight"))

    def test_inputDirectoryExistFrontBack(self):
        self.assertTrue(os.path.isdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack"))

    def test_outputDirectoryOnlyLeftLungExist(self):
        self.assertTrue(os.path.isdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung"))

    def test_outputDirectoryOnlyRightLungExist(self):
        self.assertTrue(os.path.isdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung"))

    def test_LeftLungoutputDirectoryNotEmptyTopBottom(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\TopBottom")),
                            0)

    def test_LeftLungoutputDirectoryNotEmptyFrontBack(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\FrontBack")),
                            0)

    def test_LeftLungoutputDirectoryNotEmptyLeftRight(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung\\LeftRight")),
                            0)

    def test_LeftLungOutputDirectoryNotEmpty(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyLeftLung")), 0)

    def test_RightLungOutputDirectoryNotEmptyTopBottom(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\TopBottom")),
                            0)

    def test_RightLungOutputDirectoryNotEmptyFrontBack(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\FrontBack")),
                            0)
    def test_RightLungOutputDirectoryNotEmptyLeftRight(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung\\LeftRight")),
                            0)
    def test_RightLungOutputDirectoryNotEmpty(self):
        self.assertNotEqual(len(os.listdir(
            "C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\OnlyRightLung")), 0)

    def test_inputDirectoriesNotEmptyTopBottom(self):
        self.assertNotEqual(len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\TopBottom")),
                            0)

    def test_inputDirectoriesNotEmptyFrontBack(self):
        self.assertNotEqual(len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\FrontBack")),
                            0)

    def  test_inputDirectoriesNotEmptyLeftRight(self):
        self.assertNotEqual(len(
            os.listdir("C:\\Users\\denis\\Desktop\\Software-Engineering2020\\TrainCTRs\\001\\Masks\\Mask1\\LeftRight")),
                            0)

    def test_isFinalDirOnEmptyDirShouldBeTrue(self):
        self.assertEqual(True, isFinalDir("C:\\Users\\denis\\Desktop\\ForTests\\FrontBack"))

    def test_isCTR_dir(self):
        self.assertEqual(-1, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\forIsCTRFolder"))

    def test_inputFolderNotEmpty(self):
        self.assertEqual(-2, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\FrontBack"))

    def test_notCTRinName(self):
        self.assertEqual(-3, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\notCTRFiles\\FrontBack"))

    def test_imagesNotOfSize512ShouldReturnMinusFour(self):
        self.assertEqual(-4, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\notSize512\\FrontBack"))

    def test_SplitFrontBack(self):
        self.assertEqual(1, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\ShouldWork\\Mask1\\FrontBack"))

    def test_SplitLeftRight(self):
        self.assertEqual(0, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\ShouldWork\\Mask1\\LeftRight"))

    def test_SplitTopBottom(self):
        self.assertEqual(1, separateLungs("C:\\Users\\denis\\Desktop\\ForTests\\ShouldWork\\Mask1\\TopBottom"))

    def test_WorksOkOnFolders(self):
        self.assertEqual(1, splitLungs.main("C:\\Users\\denis\\Desktop\\ForTests\\TestMain"))


if __name__ == '__main__':
    unittest.main()