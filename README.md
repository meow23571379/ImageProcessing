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
![image](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/JPEG_example_subimage.svg/400px-JPEG_example_subimage.svg.png)
以上圖為例，有8x8=64個pixel。藉由計算從原本的intensity範圍重新分配到[0,255]（相同的intensity投影後必須還是相同的值），可以得到一個看似不錯的效果。為了重新分配，我們先計算每個intensity的cumulative distribution值（由小的intensity開始累加），代表此intensity在[0,255]之間的位置與0的距離比例。
可以得到下面這個式子：
![image](https://wikimedia.org/api/rest_v1/media/math/render/svg/49e7d6c2a0e08b6c363dc7df0c4acd6629d8e150)
MxN代表全部的pixel數，L代表要投影的範圍（256）。cdf/MN即代表與0的距離比例，再乘上255就會是在[0,255]中的值。取round的原因是因為intensity必為整數。而式子中分子與分母減去CDFmin是為了消去此式子中的bias。
由此可得一個重新分配intensity後的image，因為相較於原圖比較平均，因此看起來會較為顯色。
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

