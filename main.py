#!/usr/bin/env python
from optparse import OptionParser
import PIL
from PIL import Image
from PIL import ImageTk
import math
import sys

def main():
    options = parse_args()
    if options.Upside_Down:
        UpsideDown()
    elif options.Rightside_Left:
        RightsideLeft()
    elif options.Diagonally_Mirrored:
        DiagonallyMirrored()
    elif options.Binary_image:
        BinaryImage()
    elif options.Histogram:
        Histogram()




def parse_args():
    parser = OptionParser(usage="usage: %prog [-h|options] [input image filename] [output image filename]",version="%prog 09_21") 
    parser.add_option('-u', '--upsidedown',action="store_true", dest='Upside_Down', #callback=UpsideDown(),
                      help='Will turn the input file upside-down (HW1-1-1)')
    parser.add_option('-r', '--rightsideleft', action="store_true",dest='Rightside_Left',  #callback=RightsideLeft(),
                      help='Will turn the input file rightside-left (HW1-1-2)')
    parser.add_option('-d', '--diagonally', action="store_true",dest='Diagonally_Mirrored',  #callback=DiagonallyMirrored(),
                      help='Will turn the input file diagonally mirrored (HW1-1-3)')
    parser.add_option('-b', '--binarythreshold', action="store_true",dest='Binary_image',  #callback=DiagonallyMirrored(),
                      help='Will turn the input file into a binary image with a threshold (HW2-1)')
    parser.add_option('-H', '--histogram', action="store_true",dest='Histogram',  #callback=DiagonallyMirrored(),
                      help='Will turn the input file into a Histogram (HW2-2)')
    options, args = parser.parse_args() 
    if len(args) > 2:
        parser.error('Too many arguments.')
    return options

def ReadImage():
    image = Image.open(sys.argv[2])
    return image

def SaveImage(image):
    image = image.convert('RGB')
    image.save(sys.argv[3])
    return

def UpsideDown():
    image = ReadImage()
    pix = image.load()
    newImage = Image.new( 'I', (int(image.size[0]),int(image.size[1])), "black")
    pix2 = newImage.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pix2[i,j] = pix[i,image.size[1]-1-j]
    SaveImage(newImage)

def RightsideLeft():
    image = ReadImage()
    pix = image.load()
    newImage = Image.new( 'I', (int(image.size[0]),int(image.size[1])), "black")
    pix2 = newImage.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pix2[i,j] = pix[image.size[0]-1-i,j]
    SaveImage(newImage)

def DiagonallyMirrored():
    image = ReadImage()
    pix = image.load()
    newImage = Image.new( 'I', (int(image.size[0]),int(image.size[1])), "black")
    pix2 = newImage.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pix2[i,j] = pix[j,i]
    SaveImage(newImage)

def BinaryImage():
    image = ReadImage()
    pix = image.load()
    newImage = Image.new( 'I', (int(image.size[0]),int(image.size[1])), "black")
    pix2 = newImage.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if pix[i,j] >= 128:
                pix2[i,j] = 255
            else:
                pix2[i,j] = 0
    SaveImage(newImage)

def Histogram():
    image = ReadImage()
    pix = image.load()
    newImage = Image.new( 'I', (int(image.size[0]),int(image.size[1])), "black")
    pix2 = newImage.load()
    MN = image.size[0]*image.size[1]
    int_freq = [0 for x in range(256)] 
    H_freq = [0 for x in range(256)]
    new_int = [0 for x in range(256)]
    new_freq = [0 for x in range(256)]
    gmin = 0
    Hmin = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            #print(pix[i,j][k])
            int_freq[pix[i,j]]+= 1
    for i in range(256):
        if int_freq[i]:
            gmin = i
            break
    for i in range(256):
        if i:
            H_freq[i] = int_freq[i]+ H_freq[i-1]
        else:
            H_freq[0] = int_freq[0]
    Hmin = H_freq[gmin]
    for i in range(256):
        new_int[i] = round((H_freq[i]-Hmin)* 255/(MN - Hmin+1))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pix2[i,j] = int(new_int[pix[i,j]])
            new_freq[pix2[i,j]]+=1
    #show histogram
    scaling = 10
    histogram_R = Image.new( 'I', (256,256), "white")
    newMN = histogram_R.size[0]*histogram_R.size[1]
    hisR_pix = histogram_R.load()
    for j in range(256):
        #print(int_freq[0][j]*255/newMN, int_freq[1][j]*255/newMN,int_freq[2][j]*255/newMN)
        for k in range(min(int(scaling*round(int_freq[j]*255/newMN)),255)):
            hisR_pix[k,j] = 150
    SaveImage(histogram_R)

if __name__ == '__main__':
    main()


