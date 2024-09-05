#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

#### Draw a line on the image

import cv2 
image = cv2.imread("pika.png")

# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (0, 0)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (250, 250)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
  

cv2.imshow("Image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()


#### Draw a rectangle on the image
 
import cv2 
image = cv2.imread("pika.png")
  
# Start coordinate, here (5, 5) represents the top left corner of rectangle
start_point = (5, 5)
# Ending coordinate, here (220, 220) represents the bottom right corner of rectangle
end_point = (220, 220) 
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Using thickness of -1 px to fill the rectangle by black color.
import cv2
image = cv2.imread("pika.png", 1)
start_point = (100, 50)
end_point = (125, 80)
color = (0, 0, 0)
thickness = -1
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#### Draw the circle on the image

import cv2
image = cv2.imread("pika.png")

# Center coordinates
center_coordinates = (120, 50)
# Radius of circle
radius = 20
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


## Using thickness of -1 px to fill the circle by red color. 

import cv2
image = cv2.imread("pika.png")
window_name = 'Image'
center_coordinates = (120, 100)
radius = 30
color = (0, 0, 255)
thickness = -1
image = cv2.circle(image, center_coordinates, radius, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#### Draw some text on the image

# Python program to explain cv2.putText() method
	
# importing cv2
import cv2
image = cv2.imread("pika.png")

# font
font = cv2.FONT_HERSHEY_SIMPLEX
# orgin
org = (50, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
image = cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()