#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

##### Grayscaling of an image read as colored

import cv2
 
image = cv2.imread('pika.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Using averaging of pixels method to grayscale the image
# Without using the library to grayscale the image
import cv2

img = cv2.imread('pika.png')
(row, col) = img.shape[0:2]

#for i in range(row) and for j in range(col): 
#These loops iterate through each pixel in the image by row and column.

for i in range(row):              
	for j in range(col):
		# Find the average of the BGR pixel values
		img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


##### Rotating an image
import cv2

img = cv2.imread("pika.png")
(rows, cols) = img.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
#Center of Rotation ((cols / 2, rows / 2))
#Angle of Rotation (45 degrees)
#Scale (1)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('result.jpg', res)

##### Edge Detection in an image
import cv2
img = cv2.imread('pika.png')
# We are using the Canny Edge Detection Algorithm here
# No need to dive deep into explanation over here
edges = cv2.Canny(img, 100, 200)

cv2.imwrite('result.jpg', edges)



##### Convert the image from one color frame to another
# Convert an image from RGB to HSV 

# Python program to explain cv2.cvtColor() method

import cv2

image = cv2.imread('pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )

cv2.imshow("frame", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
