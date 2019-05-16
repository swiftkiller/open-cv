import cv2

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\WIN_20170902_18_09_13_Pro.jpg"

img=cv2.imread(imgpath)

cv2.imshow('Pika', img)
cv2.waitKey(0)
cv2.destroyWindow('Pika')
