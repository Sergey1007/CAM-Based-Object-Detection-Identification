import cv2
from matplotlib import pyplot



cap = cv2.VideoCapture(0)
_, img = cap.read()
print(img.shape)

pyplot.imshow(img)
pyplot.show()

#cv2.imshow('result', img)
#cv2.waitKey(5000)