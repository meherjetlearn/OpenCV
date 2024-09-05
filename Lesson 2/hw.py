# Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

# Arithmetic Operation on Images
# Pixel values are directly added / subtarcted for 2 images
# make sure that the 2 images are of same size

"""import cv2 
import numpy as np 
     
image1 = cv2.imread('input1.png') 
image2 = cv2.imread('pika.png')
  
# 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
  
cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0) 
cv2.destroyAllWindows() """

"""##### Subtraction of images

import cv2 

image1 = cv2.imread('input1.jpg') 
image2 = cv2.imread('input2.jpg')
  
sub = cv2.subtract(image1, image2)
  
cv2.imshow('Subtracted Image', sub)
  
cv2.waitKey(0)
cv2.destroyAllWindows()"""

##### Image Resizing
# Explain the various situtions where image resizing is needed

import cv2
import os

img = cv2.imread("pika_hw.png",1)
img2 = cv2.imread("fruits_hw.png",1)




weightedSum = cv2.addWeighted(img, 0.5, img2, 0.4, 0)
  
cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0) 
cv2.destroyAllWindows() 


##### Erosion of an image, corners are trimmed in erosion

