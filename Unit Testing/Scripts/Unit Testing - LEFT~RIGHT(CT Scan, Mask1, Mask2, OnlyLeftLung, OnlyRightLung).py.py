import unittest
import os
# If the path is diffrent, you need to change de path to every function (CTRL+F -> TRAIN_DIR -> Replace all with the new path)
# TRAIN_DIR = 'D:\\Git\\TrainCTRs'
# Folders that do not have the same number of images
# LEFT LUNG
#           ->FrontBack (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
#           ->TopBottom (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
#           ->LeftRight (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
# RIGHT LUNG
#           ->FrontBack (CT Scan-Mask1, Mask1-Mask2, OnlyRightLung-Mask2, OnlyRightLung-Mask1)
#           ->TopBottom (CT Scan-Mask1, Mask1-Mask2, OnlyRightLung-Mask2, OnlyRightLung-Mask1)
#           ->LeftRight (CT Scan-Mask1, Mask1-Mask2, OnlyRightLung-Mask2, OnlyRightLung-Mask1)


class TestCase(unittest.TestCase):

#LEFT LUNG
    # LEFT LUNG - FrontBack (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
    def test_LEFTFrontBackCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO =0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[LEFT/FrontBack]Numar diferit CT Scan - Mask1")
    def test_LEFTFrontBackMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[LEFT/FrontBack]Numar diferit Mask1 - Mask2")
    def test_LEFTFrontBackMask1OnlyLeftLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO =0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2, "[LEFT/FrontBack]Numar diferit Mask1OnlyLeftLung - Mask2")
    def test_LEFTFrontBackMask1OnlyLeftLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO =0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1, "[LEFT/FrontBack]Numar diferit Mask1OnlyLeftLung - Mask1")


    # LEFT LUNG - TopBottom (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
    def test_LEFTTopBottomCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[LEFT/TopBottom]Numar diferit CT Scan - Mask1")
    def test_LEFTTopBottomMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[LEFT/TopBottom]Numar diferit Mask1 - Mask2")
    def test_LEFTTopBottomMask1OnlyLeftLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2, "[LEFT/TopBottom]Numar diferit Mask1OnlyLeftLung - Mask2")
    def test_LEFTTopBottomMask1OnlyLeftLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO =0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1, "[LEFT/TopBottom]Numar diferit Mask1OnlyLeftLung - Mask1")

    # LEFT LUNG - LeftRight (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2)
    def test_LEFTLeftRightCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[LEFT/LeftRight]Numar diferit CT Scan - Mask1")
    def test_LEFTLeftRightMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[LEFT/LeftRight]Numar diferit Mask1 - Mask2")
    def test_LEFTLeftRightMask1OnlyLeftLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2, "[LEFT/LeftRight]Numar diferit Mask1OnlyLeftLung - Mask2")
    def test_LEFTLeftRightMask1OnlyLeftLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO =0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyLeftLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1, "[LEFT/LeftRight]Numar diferit Mask1OnlyLeftLung - Mask1")


#RIGHT LUNG
        # RIGHT LUNG - FrontBack (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
    def test_RIGHTFrontBackCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\FrontBack')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[RIGHT/FrontBack]Numar diferit CT Scan - Mask1")

    def test_RIGHTFrontBackMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[RIGHT/FrontBack]Numar diferit Mask1 - Mask2")

    def test_RIGHTFrontBackMask1OnlyRightLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2,"[RIGHT/FrontBack]Numar diferit Mask1OnlyRightLung - Mask2")

    def test_RIGHTFrontBackMask1OnlyRightLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO = 0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\FrontBack')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1,"[RIGHT/FrontBack]Numar diferit Mask1OnlyRightLung - Mask1")

    # RIGHT LUNG - TopBottom (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2, OnlyLeftLung-Mask1)
    def test_RIGHTTopBottomCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\TopBottom')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[RIGHT/TopBottom]Numar diferit CT Scan - Mask1")

    def test_RIGHTTopBottomMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[RIGHT/TopBottom]Numar diferit Mask1 - Mask2")

    def test_RIGHTTopBottomMask1OnlyRightLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2,"[RIGHT/TopBottom]Numar diferit Mask1OnlyRightLung - Mask2")

    def test_RIGHTTopBottomMask1OnlyRightLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO = 0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\TopBottom')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1,"[RIGHT/TopBottom]Numar diferit Mask1OnlyRightLung - Mask1")

    # RIGHT LUNG - LeftRight (CT Scan-Mask1, Mask1-Mask2, OnlyLeftLung-Mask2)
    def test_RIGHTLeftRightCTScanMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaCTScan = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfoldersCTScan = sub[-3:]
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            pathMask = os.path.join(TRAIN_DIR, sub[-3:] + '\\CT Scan\\LeftRight')
            for root1, dirs1, files1 in os.walk(pathMask):
                for name1 in files:
                    nume_poza_CTScan = name1
                    countNumePozaCTScan = countNumePozaCTScan + 1
        self.assertEqual(countNumePozaCTScan, countNumePozaMask, "[RIGHT/LeftRight]Numar diferit CT Scan - Mask1")

    def test_RIGHTLeftRightMask1Mask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask = countNumePozaMask + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMask, countNumePozaMask2, "[RIGHT/LeftRight]Numar diferit Mask1 - Mask2")

    def test_RIGHTLeftRightMask1OnlyRightLungMask2(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMask = 0
        countNumePozaMaskO = 0
        countNumePozaMask2 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask2\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask2 = countNumePozaMask2 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask2,"[RIGHT/LeftRight]Numar diferit Mask1OnlyRightLung - Mask2")

    def test_RIGHTLeftRightMask1OnlyRightLungMask1(self):
        TRAIN_DIR = 'D:\\Git\\TrainCTRs'
        countNumePozaMaskO = 0
        countNumePozaMask1 = 0
        subfolders = [f.path for f in os.scandir(TRAIN_DIR) if f.is_dir()]
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\OnlyRightLung\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMaskO = countNumePozaMaskO + 1
        for sub in subfolders:
            # print(sub[-3:])
            subfodersMask = sub[-3:]
            path = os.path.join(TRAIN_DIR, sub[-3:] + '\\Masks\\Mask1\\LeftRight')
            # D:\Git\TrainCTRs\001\Masks\Mask1\FrontBack
            for root, dirs, files in os.walk(path):
                for name in files:
                    nume_poza_mask = name
                    countNumePozaMask1 = countNumePozaMask1 + 1
        self.assertEqual(countNumePozaMaskO, countNumePozaMask1,"[RIGHT/LeftRight]Numar diferit Mask1OnlyRighttLung - Mask1")


if __name__ == '__main__':
    unittest.main()
