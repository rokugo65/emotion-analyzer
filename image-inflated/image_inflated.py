import os
import re
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageOps, ImageEnhance

def saveImage(_inImg,_inExportPath):
    files = os.listdir(_inExportPath)
    imgNum = 1
    for file in files:
        index = re.search('.png',file)
        if index:
            imgNum += 1
    exportImagePath = os.path.join(_inExportPath,str(imgNum)+'.png')
    _inImg.save(exportImagePath)

def changeColorRate(_inImg,_inRateRed,_inRateGreen,_inRateBlue):
    h = _inImg.size[1] 
    w = _inImg.size[0]
    _outImg = Image.new('RGB',(w,h))
    for x in range(w):
        for y in range(h):
            r,g,b = _inImg.getpixel((x,y))
            r = r * _inRateRed
            g = g * _inRateGreen
            b = b * _inRateBlue
            _outImg.putpixel((x,y),(int(r),int(g),int(b)))
    return _outImg

def imageInflated(_inImportPath, _inExportPath):
    files = os.listdir(_inImportPath)
    imgNum = 0
    for file in files:
        index = re.search('.png',file)
        if index:
            imgNum += 1

    print(imgNum)

    for i in range(imgNum):

        importImagePath = os.path.join(_inImportPath,str(i+1)+'.png')
        im_0 = Image.open(importImagePath)
        saveImage(im_0,_inExportPath)

        im_1 = ImageOps.mirror(im_0)
        saveImage(im_1,_inExportPath)

        im_2 = im_0.point(lambda x:x * 1.3)
        saveImage(im_2,_inExportPath)

        im_3 = im_1.point(lambda x:x * 1.3)
        saveImage(im_3,_inExportPath)

        im_4 = im_0.point(lambda x:x * 0.7)
        saveImage(im_4,_inExportPath)

        im_5 = im_1.point(lambda x:x * 0.7)
        saveImage(im_5,_inExportPath)

        im_6 = changeColorRate(im_0,1.2,1,1)
        saveImage(im_6,_inExportPath)

        im_8 = changeColorRate(im_1,1.2,1,1)
        saveImage(im_8,_inExportPath)

        im_7 = changeColorRate(im_0,0.8,1,1)
        saveImage(im_7,_inExportPath)

        im_9 = changeColorRate(im_1,0.8,1,1)
        saveImage(im_9,_inExportPath)

        im_10 = changeColorRate(im_0,1,1.2,1)
        saveImage(im_10,_inExportPath)

        im_12 = changeColorRate(im_1,1,1.2,1)
        saveImage(im_12,_inExportPath)

        im_11 = changeColorRate(im_0,1,0.8,1)
        saveImage(im_11,_inExportPath)

        im_13 = changeColorRate(im_1,1,0.8,1)
        saveImage(im_13,_inExportPath)

        im_14 = changeColorRate(im_0,1,1,1.2)
        saveImage(im_14,_inExportPath)

        im_16 = changeColorRate(im_1,1,1,1.2)
        saveImage(im_16,_inExportPath)

        im_15 = changeColorRate(im_0,1,1,0.8)
        saveImage(im_15,_inExportPath)

        im_17 = changeColorRate(im_1,1,1,0.8)
        saveImage(im_17,_inExportPath)

        iec_1 = ImageEnhance.Contrast(im_0)
        im_18 = iec_1.enhance(1.3)
        saveImage(im_18,_inExportPath)

        iec_2 = ImageEnhance.Contrast(im_1)
        im_19 = iec_2.enhance(1.3)
        saveImage(im_19,_inExportPath)

        iec_3 = ImageEnhance.Contrast(im_0)
        im_20 = iec_3.enhance(0.7)
        saveImage(im_20,_inExportPath)

        iec_4 = ImageEnhance.Contrast(im_1)
        im_21 = iec_4.enhance(0.7)
        saveImage(im_21,_inExportPath)

        iec_5 = ImageEnhance.Color(im_0)
        im_22 = iec_5.enhance(1.3)
        saveImage(im_22,_inExportPath)

        iec_6 = ImageEnhance.Color(im_1)
        im_23 = iec_6.enhance(1.3)
        saveImage(im_23,_inExportPath)

        iec_7 = ImageEnhance.Color(im_0)
        im_24 = iec_7.enhance(0.7)
        saveImage(im_24,_inExportPath)

        iec_8 = ImageEnhance.Color(im_1)
        im_25 = iec_8.enhance(0.7)
        saveImage(im_25,_inExportPath)

        iec_9 = ImageEnhance.Sharpness(im_0)
        im_26 = iec_9.enhance(2)
        saveImage(im_26,_inExportPath)

        iec_10 = ImageEnhance.Sharpness(im_1)
        im_27 = iec_10.enhance(2)
        saveImage(im_27,_inExportPath)

        iec_11 = ImageEnhance.Sharpness(im_0)
        im_28 = iec_11.enhance(0.3)
        saveImage(im_28,_inExportPath)

        iec_12 = ImageEnhance.Sharpness(im_1)
        im_29 = iec_12.enhance(0.3)
        saveImage(im_29,_inExportPath)




if __name__ == '__main__':
    importPath = os.path.join('import','anger')
    exportPath = os.path.join('export','anger')
    imageInflated(importPath, exportPath)
    
    importPath = os.path.join('import','contempt')
    exportPath = os.path.join('export','contempt')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','disgust')
    exportPath = os.path.join('export','disgust')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','fear')
    exportPath = os.path.join('export','fear')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','happiness')
    exportPath = os.path.join('export','happiness')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','neutral')
    exportPath = os.path.join('export','neutral')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','sadness')
    exportPath = os.path.join('export','sadness')
    imageInflated(importPath, exportPath)

    importPath = os.path.join('import','surprise')
    exportPath = os.path.join('export','surprise')
    imageInflated(importPath, exportPath)

