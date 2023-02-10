import cv2
import os
import pytesseract
from PIL import Image

#https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd
#https://pythonhosted.org/PyDrive/pydrive.html#pydrive.files.GoogleDriveFile.GetContentFile

#https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderrors
#https://pyimagesearch.com/2021/10/27/automatically-ocring-receipts-and-scans/

#https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/
#https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html

#Reading - a folder of images from googledrive
#imlist = []
#filelist = []
#for file in glob.glob(r"C:\Users\Andrew Hu\Dropbox\PC\Desktop\*.jpg"):
 #   IM = cv.imread(file)
  #  imlist.append(IM)
   # filelist.append(file)


# Reading - single image path
path = 'C:/Users/andre/Documents/IMG_6588.jpg' #path changing
img = cv2.imread(path)

# convert to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 200) # printing edged, shows the black and with contours to remap the four corners
contimg = cv2.convertScaleAbs(gray, alpha=1.2, beta=40) #1.0 - 3.0, then #0-100
#alpha of 1.2 works best, and beta 40 works best
imagetostring = contimg
options = "--psm 4"


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(imagetostring,
	config=options)
print(text)

#cv2.imshow("edge for troubleshooting", edged)
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", newimage)
cv2.waitKey(0)