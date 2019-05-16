import cv2
import numpy as np

img = cv2.imread('C:\\Users\\spars\\OneDrive\\Pictures\\set\\1.1.12.tiff')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('pika',gray)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,5000,0.5,10)
corners = np.int0(corners)

for corner in corners:
	x,y =corner.ravel()
	cv2.circle(img,(x,y),2,(0,255,0),-1)

cv2.imshow('Corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()	 

