import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

def find_numberplate():
    #Windows
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    #M1
    #ytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/4.1.1/bin/tesseract'

    #Import image and resize it
    #Aygo
    #img = cv2.imread('./images/aygo.png', cv2.IMREAD_COLOR)
    #img = imutils.resize(img, width=610)

    #Tesla
    img = cv2.imread('./images/tesla.jpg', cv2.IMREAD_COLOR)
    img = imutils.resize(img, width=600)

    #Gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Blur to reduce noise
    gray = cv2.bilateralFilter(gray, 13, 15, 15)

    #Edge detection
    edged = cv2.Canny(gray, 30, 200)

    contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None

    #Find contours in the edged image
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]

    NumberPlateCnt = None 
    count = 0
    #Loop over contours
    for c in cnts:
        #Approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        #If the approximated contour has four points, then assume that screen is found
        if len(approx) == 4:  
            NumberPlateCnt = approx 
            break

    #Mask the part other than the numberplate
    mask = np.zeros(gray.shape,np.uint8)
    new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
    new_image = cv2.bitwise_and(img,img,mask=mask)

    #Crop the image 
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx+1, topy:bottomy+1]

    #Read the number plate
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(Cropped, config=config)
    print("Nummerpladen er:",text)
    plt.imshow(new_image)

    cv2.waitKey(1)
    cv2.destroyAllWindows() 

    return text