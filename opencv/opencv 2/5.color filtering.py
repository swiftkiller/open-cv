import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	rev,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([90,0,50])
	upper_red = np.array([120,250,255])

	mask = cv2.inRange(hsv,lower_red,upper_red)
	res = cv2.bitwise_and(frame,frame,mask=mask )

	cv2.imshow('frame',frame)
	cv2.imshow('res',res)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		
