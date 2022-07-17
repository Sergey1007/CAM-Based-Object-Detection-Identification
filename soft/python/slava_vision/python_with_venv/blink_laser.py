import cv2

img1 = cv2.imread('sources/img1.jpg')
img2 = cv2.imread('sources/img2.jpg')
img3 = cv2.imread('sources/img3.jpg')
img4 = cv2.imread('sources/img4.jpg')
img5 = cv2.imread('sources/img5.jpg')

img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))
img3 = cv2.resize(img3, (640, 480))
img4 = cv2.resize(img4, (640, 480))
img5 = cv2.resize(img5, (640, 480))

img1 = cv2.GaussianBlur(img1, (5, 5), 3)
img2 = cv2.GaussianBlur(img2, (5, 5), 3)
img3 = cv2.GaussianBlur(img3, (5, 5), 3)
img4 = cv2.GaussianBlur(img4, (5, 5), 3)
img5 = cv2.GaussianBlur(img5, (5, 5), 3)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
gray5 = cv2.cvtColor(img5, cv2.COLOR_BGR2HSV)

# cv2.imshow('gray1',gray1)
# cv2.imshow('gray2',gray2)


xor1 = cv2.bitwise_xor(gray1, gray2)
xor1 = cv2.cvtColor(xor1, cv2.COLOR_BGR2GRAY)
# cv2.imshow('xor',xor1)


xor2 = cv2.bitwise_xor(gray2, gray3)
xor2 = cv2.cvtColor(xor2, cv2.COLOR_BGR2GRAY)
# cv2.imshow('xor',xor2)

xor3 = cv2.bitwise_xor(gray3, gray4)
xor3 = cv2.cvtColor(xor3, cv2.COLOR_BGR2GRAY)
# cv2.imshow('xor',xor3)

xor4 = cv2.bitwise_xor(gray4, gray5)
xor4 = cv2.cvtColor(xor4, cv2.COLOR_BGR2GRAY)
# cv2.imshow('xor',xor2)


threshold1, thresh1 = cv2.threshold(xor1, 100, 255, cv2.THRESH_BINARY)
threshold2, thresh2 = cv2.threshold(xor2, 100, 255, cv2.THRESH_BINARY)
threshold1, thresh3 = cv2.threshold(xor3, 100, 255, cv2.THRESH_BINARY)
threshold2, thresh4 = cv2.threshold(xor4, 100, 255, cv2.THRESH_BINARY)

thresh_1 = cv2.bitwise_and(thresh1, thresh2)
thresh_2 = cv2.bitwise_and(thresh3, thresh4)
thresh = cv2.bitwise_and(thresh_1, thresh_2)

cv2.imshow('thresh', thresh)

thresh = cv2.erode(thresh, (3, 3), iterations=3)
cv2.imshow('thresh', thresh)

moments = cv2.moments(thresh, 1)
dM01 = moments['m01']
dM10 = moments['m10']
dArea = moments['m00']
x = int(dM10 / dArea)
y = int(dM01 / dArea)

print(x, y)
cv2.circle(img2, (x, y), 10, (255, 0, 0), -1)
cv2.imshow('result', img2)

cv2.waitKey(5000)
