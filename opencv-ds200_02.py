import cv2 as cv
import numpy as np

#######################################
#Auxillary code, run with same file to determine micron:pixel ratio
#IN DOWNLOADS IMG_002DS RANDOM 100x image, so crop it to find counter for legend pixel size
#very janky still, could optimize
#######################################

path = 'C:/Users/andre/Downloads/IMG_002DS.jpg'
img = cv.imread(path)
theta = 0


legendy = 1400
legendyend = 2048-400
legendx = 1790
legendxend = 2048
img = img[legendy:legendyend, legendx:legendxend]

newimg = cv.convertScaleAbs(img, alpha=1.6, beta=99) #alpha from 1.0-3.0 #beta from 0-100
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
shape = ( img.shape[1], img.shape[0] ) # cv2.warpAffine expects shape in (length, height)
matrix = cv.getRotationMatrix2D( center=(x,y), angle=theta, scale=1 )
CROP = cv.warpAffine( src=img, M=matrix, dsize=shape )
xnew = int( x - width/2  )
ynew = int( y - height/2 )

## below visualize the contours to help with debugging
cv.drawContours(newimg, contours, -1, (0,255,0), 3) #draws all contours found
cv.drawContours(newimg, [cnt], 0, (0,255,0), 3) #draws the largest contour
cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3) #draws the rectangle found

cv.imshow('Working Image', newimg)
cv.imshow('Output Image', img)
cv.imshow('CROP',CROP)
#cv.waitKey(0)

print("legend bar pixels: {}, legend bar pixels (height): {}".format(w, h))
