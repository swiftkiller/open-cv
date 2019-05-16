import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	w = 160
	h = 120

	windowName='Live Video'
	cv2.namedWindow(windowName)
	cap=cv2.VideoCapture(0)

	cap.set(3,w)
	cap.set(4,h)

	if cap.isOpened():
	    ret, frame = cap.read()
	    print(frame)   
	else:
	    ret = False


	while ret:
		ret, frame = cap.read()

		z = frame.reshape((-1,1))
		z = np.float32(z)

		creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

		k = 32
		ret, label1,center1 = cv2.kmeans(z,k,None,creteria,10,cv2.KMEANS_RANDOM_CENTERS)
		center1 = np.uint8(center1)
		res1 = center1[label1.flatten()]
		output1 =  res1.reshape((frame.shape))

		cv2.imshow(windowName, output1)

		if cv2.waitKey(1)==27:
		    break 
	cv2.destroyWindow(windowName)
	cap.release()

if __name__=="__main__":
    main()    