import cv2
import numpy as np
from matplotlib import pyplot

def get_red_xy(img):
    finish_list=[]
    low_blue = np.array((170, 150, 100), np.uint8)
    high_blue = np.array((180, 255, 255), np.uint8)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_blue = cv2.inRange(img_hsv,low_blue, high_blue)
    #result = cv2.bitwise_and(img_hsv,img_hsv,mask = mask_blue)
    moments = cv2.moments(mask_blue, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    x = int(dM10 / dArea)
    y = int(dM01 / dArea)
    finish_list.append(x)
    finish_list.append(y)

    return finish_list





if __name__=="__main__":
    while True:
        #img = cv2.imread('sources/ipad1.jpg'
        cap = cv2.VideoCapture(0)
        fl, img = cap.read()
        print(fl)
        if fl==True:
            try:
                result=get_red_xy(img)
                print(result)
                cv2.circle(img, result, 10, (255, 0, 0), -1) #you can draw a found point
                cv2.imshow('result',img)
                cv2.waitKey(1000)
            except ZeroDivisionError:
                print('error zero division')