
# Refer - https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/

#### Create a Video Collage (Video created out of images)

import os
import cv2
from PIL import Image # Pillow - Image Processing Library Python Imaging Library
import PIL
#to check PIL version
print(PIL.__version__)

# Change the directory as per own folder path where the images are located
os.chdir('C:\\Users\\gayat\\Documents\\python\\openCV\\Lesson 5\\photos')
path = "C:\\Users\\gayat\\Documents\\python\\openCV\\Lesson 5\\photos"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.')) # 7

# for calculating avg width and height
#we need to do this 
#because the video which will be created using cv2 library 
# requires the input images of same height and width.
for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height


mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

#This loop iterates through each image in the directory, 
# resizes it to the average dimensions  and saves the resized image.
#Image.Resampling.LANCZOS is used for high-quality image resizin

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)
         
        
        #if PIL version is above 10.0 Lanczos need to used  else antialias
        #imgResized = img.resize((mean_width, mean_height), Image.ANTIALIAS)
        imgResized = img.resize((mean_width, mean_height), Image.Resampling.LANCZOS)
        imgResized.save(file, 'png', quality = 95)

        #[-1]: This retrieves the last element of the entire file path name,
        #  which would be the file name itself (image.jpg in this case).
        # print(img.filename, " is resized") entire path

        #[-1]: This retrieves the last element of the entire file path name,
        #  which would be the file name itself 
        print(img.filename.split('\\')[-1], " is resized")

        

def videoGenerator():
    video_name = "hw.avi"

    os.chdir('C:\\Users\\gayat\\Documents\\python\\openCV\\Lesson 5\\photos')

    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)
    
    # Array images should only consider the image files ignoring others if any
    print(images)
    
    frame = cv2.imread(os.path.join(".", images[0]))

     # setting the frame width, height width the width, height of first image
    height, width, layers = frame.shape

    #0 is the encoding technique
    #1 in videowriter means the video will play at 1 frame per second
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    
    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()

videoGenerator()
