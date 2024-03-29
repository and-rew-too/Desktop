import cv2 as cv
import numpy as np

path = 'C:/Users/andre/Downloads/IMG_001DS.jpg'
img = cv.imread(path)

width = 604
height = 453
dim = (604,453)
buffer = 7*15//10
theta = 0

img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
img = img[0:284, 0:453]
imgr = img
# scale_percent = 15 #enter percentage of original size
# buffer = 7*scale_percent//10 #set to 0 for the standard cropping in opencv
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
#
#cv.imshow('Output Image', img)
#cv.waitKey(0)
#imgr = cv.cvtColor(imgr, cv.COLOR_BGR2GRAY)


newimg = cv.convertScaleAbs(imgr, alpha=0.6, beta=41) #alpha from 1.0-3.0 #beta from 0-100
height, width = img.shape[0], img.shape[1]
print("width: {}, height: {}".format(width, height))


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
cv.imshow('Output Image', imgr)
#cv.imshow('CROP',cropped)
cv.waitKey(0)
