#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

#### Draw a line on the image

import cv2 
image = cv2.imread("pika.png")

# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (0, 250)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (500, 250)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image1 = cv2.line(image, start_point, end_point, color, thickness)

image2 = cv2.line(image1, (0,250), (200,125), color, thickness)
image3 = cv2.line(image2, (200,125), (425,250), color, thickness)
image4 = cv2.rectangle(image3, (0, 250), (410,410), (255, 255, 0), thickness)  




#### Draw a rectangle on the image
 

  
cv2.imshow("Image", image4)
cv2.waitKey(0)
cv2.destroyAllWindows()







