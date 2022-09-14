import cv2 as cv
import numpy as np

#######################################
#Core code that finds the circular contour of print laid down
#outputs the final pixels of dielectric print (WHEN KEYENCE IS SET TO FULL RING)
#need to run with opencv-ds200_02 to convert pixels to microns
#######################################


path = 'C:/Users/andre/Downloads/IMG_002DS.jpg'
img = cv.imread(path)
#dim = (2048,1536)
buffer = 7*15//10
theta = 0

#img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
#img = img[0:284, 0:453] #line where the image is cropped
imgr = img


newimg = cv.convertScaleAbs(imgr, alpha=1.6, beta=99) #alpha from 1.0-3.0 #beta from 0-100
# alpha set to 1.9 and beta set to 20-80
height, width = img.shape[0], img.shape[1]
print("image width: {}, image height: {}".format(width, height))


imgray = cv.cvtColor(newimg, cv.COLOR_BGR2GRAY) #line 22-24 finds contours in grayscale
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


size = [] #line 27-34 iterate through contours, lengths of contour, then index the largest one (the actual module)
for i in range(0,len(contours)):
    size.append(len(contours[i]))
print(size)
print(max(size))
print(size.index(max(size)))
largest = size.index(max(size))
cnt = contours[largest] #cnt most important variable, using this a ton

(x,y,w,h) = cv.boundingRect(cnt)
cropped = imgr[y-buffer:y+h+buffer, x-buffer:x+w+buffer]
shape = ( cropped.shape[1], cropped.shape[0] ) # cv2.warpAffine expects shape in (length, height)
matrix = cv.getRotationMatrix2D( center=(x,y), angle=theta, scale=1 )
cropped = cv.warpAffine( src=cropped, M=matrix, dsize=shape )
xnew = int( x - width/2  )
ynew = int( y - height/2 )
cropped = cropped[ynew:ynew+height, xnew:xnew+width]


## below visualize the contours to help with debugging
cv.drawContours(newimg, contours, -1, (0,255,0), 3) #draws all contours found
cv.drawContours(newimg, [cnt], 0, (0,255,0), 3) #draws the largest contour
cv.rectangle(imgr,(x,y),(x+w,y+h),(255,0,0),3) #draws the rectangle found

cv.imshow('Working Image', newimg)
cv.imshow('Output Image', img)
cv.imshow('CROP',cropped)
cv.waitKey(0)

#PRINT THIS SIZE relatve to the number of pixels for
#PRINTS THIS width and
print(w)
print(h)
