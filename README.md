# ImageProcessing
Processing grey images [bmp,jpg,jpeg,png...] with algorithms

# Requirements
- PIL  https://stackoverflow.com/a/20061019

# Usage
see ```python main.py -h```for details.

## Up-side-down
Turn an image by 180 degrees.  Top to bottom, bottom to top.
```
python main.py -u /path/to/input-image /path/to/output-image
```

## Right-side-left
Mirror an image. Right to left, left to right.
```
python main.py -r /path/to/input-image /path/to/output-image
```

## Diagonally Mirrored 
Diagonally mirror an image. For example, the pixel on the left-bottom side will come to the right-top side.
```
python main.py -d /path/to/input-image /path/to/output-image
```
## Binary Threshold Image
Create a binary image of input file with 128 intensity value as threshold.
```
python main.py -b /path/to/input-image /path/to/output-image
```
## Histogram
Build a Histogram of input image.  The upper represents the lower intensity.
(Note that the option is written in large character)
```
python main.py -H /path/to/input-image /path/to/output-image
```
## Histogram Equalization
Histogram equalization is a method in image processing of contrast adjustment using the image's histogram.
Users will get a better image by redistributing the intensities, a.k.a. brightness.
(Note that the option is written in large character)
```
python main.py -E /path/to/input-image /path/to/output-image
```
(todo list)
## Connected Components

-----------------------
## Erosion

## Dilation

## Complement

## Smoothing

## Edging

## Amplification

## Shrinking

## Rotaion

