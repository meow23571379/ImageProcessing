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



def parse_args():
    parser = OptionParser(usage="usage: %prog [-h|options] [input image filename] [output image filename]",version="%prog 09_21") 
    parser.add_option('-U', '--upsidedown',action="store_true", dest='Upside_Down', #callback=UpsideDown(),
                      help='Will turn the input file upside-down (HW1-1-1)')
    parser.add_option('-R', '--rightsideleft', action="store_true",dest='Rightside_Left',  #callback=RightsideLeft(),
                      help='Will turn the input file rightside-left (HW1-1-2)')
    parser.add_option('-D', '--diagonallymirrored', action="store_true",dest='Diagonally_Mirrored',  #callback=DiagonallyMirrored(),
                      help='Will turn the input file diagonally mirrored (HW1-1-3)')
    
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

if __name__ == '__main__':
    main()


