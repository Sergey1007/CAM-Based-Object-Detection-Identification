import cv2

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    print(img.shape)
    img=cv2.flip(img,1)


    cv2.imshow('result', img)
    cv2.waitKey(1)