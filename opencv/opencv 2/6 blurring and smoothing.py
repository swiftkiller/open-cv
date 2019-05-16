import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	rev,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower = np.array([90,50,90])
	upper = np.array([120,250,255])

	mask = cv2.inRange(hsv,lower,upper)
	res = cv2.bitwise_and(frame,frame,mask=mask )

	denoised = cv2.medianBlur(res,5)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	cv2.imshow('denoised',denoised)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		
