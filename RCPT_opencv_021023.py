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
edged = cv2.Canny(blurred, 75, 200)
# printing edged, shows the black and with contours to remap the four corners of a skewed image

def automatic_brightness_and_contrast(image, clip_hist_percent=25):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)

    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))

    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0

    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1

    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1

    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha
    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    auto_result = cv2.cvtColor(auto_result, cv2.COLOR_BGR2GRAY)
#    auto_result = image
    return (auto_result, alpha, beta)

image = cv2.imread(path)
auto_result, alpha, beta = automatic_brightness_and_contrast(image)
print('alpha', alpha)
print('beta', beta)
cv2.imshow('auto_result', auto_result)

# show the output images
#cv2.imshow("edge for troubleshooting", edged)
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)

cv2.waitKey(0)