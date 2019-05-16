import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	rev,img = cap.read()

	Laplacian = cv2.Laplacian(img, -1, ksize=3, scale=1, delta=0, borderType = cv2.BORDER_DEFAULT)
	
	sobelx = cv2.Sobel(img, -1, dx=2,dy=0,ksize = 11, scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	sobely = cv2.Sobel(img, -1, dx=0,dy=2,ksize = 11, scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	sobel = sobelx + sobely

	scharrx = cv2.Scharr(img, -1, dx=1,dy=0,scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	scharry = cv2.Scharr(img, -1, dx=0,dy=1,scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	scharr = scharrx + scharry

	L1 = cv2.Canny(img, 100, 200, L2gradient = False)
	L2 = cv2.Canny(img , 30, 100, L2gradient = True)

	cv2.imshow('img',img)
	cv2.imshow('Laplacian',Laplacian)
	cv2.imshow('L1',L1)
	cv2.imshow('L2',L2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		
