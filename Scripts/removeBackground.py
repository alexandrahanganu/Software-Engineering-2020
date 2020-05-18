import sys
import os
from PIL import Image

def isFinalDir(inputDir):
    for fname in os.listdir(inputDir):
        if os.path.isdir(os.path.join(inputDir, fname)):
            return False
    return True

def main(argv):
    rootdir = "C:\\Users\\denis\\Desktop\\Make Transparent"
    for subdir, dirs, files in os.walk(rootdir):
        if isFinalDir(subdir):
            if "backup" in subdir:
                os.makedirs(os.path.dirname(subdir) + "\\NoBackground\\FrontBack")
            if "LeftRight" in subdir:
                os.makedirs(os.path.dirname(subdir) + "\\NoBackground\\LeftRight")
            if "TopBottom" in subdir:
                os.makedirs(os.path.dirname(subdir) + "\\NoBackground\\TopBottom")

            for file in files:
                blackBkg = Image.open(subdir + "\\" + file).convert('RGBA')
                pixels = list(blackBkg.getdata())
                newPixels = []
                for i, pixel in enumerate(pixels):
                    if 512 < i < 261632 and pixels[i] == (0, 0, 0, 255) and pixels[i - 1] == (0, 0, 0, 255) and pixels[i + 1] == (0, 0, 0, 255)\
                            and pixels[i-512] == (0, 0, 0, 255) and pixels[i+512] == (0, 0, 0, 255) and pixels[i -513] == (0, 0, 0, 255):
                        newPixels.insert(i, (0, 0, 0, 0))
                    else:
                        newPixels.insert(i, pixels[i])

                blackBkg.putdata(newPixels)
                if "backup" in subdir:
                    blackBkg.save(os.path.dirname(subdir) + "\\NoBackground\\FrontBack\\" + file)
                if "LeftRight" in subdir:
                    blackBkg.save(os.path.dirname(subdir) + "\\NoBackground\\LeftRight\\" + file)
                if "TopBottom" in subdir:
                    blackBkg.save(os.path.dirname(subdir) + "\\NoBackground\\TopBottom\\" + file)


if __name__ == '__main__':
    main(sys.argv[1:])
