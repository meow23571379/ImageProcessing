import numpy as np
import PIL
from PIL import Image
from PIL import ImageTk
import math
import sys
import cv2
image = cv2.imread("lena.bmp", cv2.IMREAD_GRAYSCALE)
thresh = 127
image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]


print(image)
print(image.shape)
newImage = np.zeros((image.shape[0]+4,image.shape[1]+4))


kernel = np.ones((5,5))
kernel[0][0] = 0
kernel[4][0] = 0
kernel[4][4] = 0
kernel[0][4] = 0

# kernel = np.zeros((5,5))
# kernel[2, 2] = 4
# kernel[1, 2] = -1
# kernel[3, 2] = -1
# kernel[2, 1] = -1
# kernel[2, 3] = -1

for i in range(2,image.shape[0]-2):
    for j in range(2,image.shape[1]-2):
        mult = kernel * image[i-2:i+3, j-2:j+3]
        if np.sum(mult) == 255 * 21:
            newImage[i][j] = 255
        # newImage[i][j] = np.sum(mult)
cv2.imshow('image',image)
cv2.imshow('newImage',newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# image = image.convert('RGB')
# image.save(sys.argv[2])
