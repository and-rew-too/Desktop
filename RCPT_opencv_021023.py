import cv2
import os,argparse
import pytesseract
from PIL import Image

#https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd
#https://pythonhosted.org/PyDrive/pydrive.html#pydrive.files.GoogleDriveFile.GetContentFile

#https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderrors
#https://pyimagesearch.com/2021/10/27/automatically-ocring-receipts-and-scans/

#https://www.geeksforgeeks.org/reading-text-from-the-image-using-tesseract/
#https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html

imlist = []
filelist = []
#for a whole folder below
#for file in glob.glob(r"C:\Users\Andrew Hu\Dropbox\PC\Desktop\*.jpg"):
 #   IM = cv.imread(file)
  #  imlist.append(IM)
   # filelist.append(file)


# We then read the image with text
path = 'C:/Users/andre/Documents/IMG_6588.jpg'
images = cv2.imread(path)

# convert to grayscale image
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
edged = cv2.Canny(blurred, 75, 200) # printing edged, shows the black and with contours to remap the four corners


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
options = "--psm 4"
text = pytesseract.image_to_string(gray,
	config=options)
print(text)

# show the output images
#cv2.imshow("edge for troubleshooting", edged)
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)