import cv2

cap = cv2.VideoCapture(0)
_, img = cap.read()
cv2.imshow('result', img)
cv2.waitKey(5000)