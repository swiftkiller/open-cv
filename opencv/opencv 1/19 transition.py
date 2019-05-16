import cv2
import numpy as np
import time

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	imgpath2= path + "WIN_20190301_18_04_19_Pro.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	for i in np.linspace(0, 1 , 1000):
		alpha = i
		beta = 1 - i
		output=cv2.addWeighted(img1, alpha, img2, beta,0)
		cv2.imshow('Tansition', output)
		time.sleep(0.005)
		if cv2.waitKey(1) == 27:
			break

	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	main()			