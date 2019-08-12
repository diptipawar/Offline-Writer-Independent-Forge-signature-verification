

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import os





def getSignatureFromPage(imgs):

    img_split = imgs.split("/")
    r = img_split[-1]
    print(r)
    img = cv2.imread(imgs)
    img = cv2.resize(img,(512,512))
    imgSize = np.shape(img)

    gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold, _ = cv2.threshold(gImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cannyImg = cv2.Canny(gImg, 0.5 * threshold, threshold)
   
    shape = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 1))
    cannyImg = cv2.morphologyEx(cannyImg, cv2.MORPH_CLOSE, shape)

    _, contours, _ = cv2.findContours(cannyImg.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    



    class Rect:
        def __init__(self, x = 0, y = 0, w = 0, h = 0):
            self.x = x
            self.y = y
            self.w = w
            self.h = h

        def getArea(self):
            return self.w * self.h
        def set(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
        def addPadding(self, imgSize, padding):
            self.x -= padding
            self.y -= padding
            self.w += 2 * padding
            self.h += 2 * padding
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0
            if self.x + self.w > imgSize[0]:
                self.w = imgSize[0] - self.x
            if self.y + self.h > imgSize[1]:
                self.h = imgSize[1] - self.y


    maxRect = Rect(0, 0, 0, 0)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        currentArea = w * h
        if currentArea > maxRect.getArea():
            maxRect.set(x, y, w, h)


    maxRect.addPadding(imgSize, 20)
    cv2.rectangle(img, (maxRect.x, maxRect.y), (maxRect.x + maxRect.w, maxRect.y + maxRect.h), (0, 0, 255), 1)

    threshold, _ = cv2.threshold(src = gImg, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cannyImg = cv2.Canny(image = gImg, threshold1 = 0.5 * threshold, threshold2 = threshold)


    kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (30, 1))
    cannyImg = cv2.morphologyEx(src = cannyImg, op = cv2.MORPH_CLOSE, kernel = kernel)


    _, contours, _ = cv2.findContours(image = cannyImg.copy(), mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)


    maxRect = Rect(0, 0, 0, 0)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(points = contour)
        currentArea = w * h
        if currentArea > maxRect.getArea():
            maxRect.set(x, y, w, h)


    maxRect.addPadding(imgSize = imgSize, padding = 20)
    
    cv2.imwrite("im/s2.jpg",img[maxRect.y : maxRect.y + maxRect.h, maxRect.x : maxRect.x + maxRect.w])

    return img[maxRect.y : maxRect.y + maxRect.h, maxRect.x : maxRect.x + maxRect.w]




signature1 = getSignatureFromPage("s2.jpg")















