import cv2
import numpy as np

def main():
	img = np.zeros((512,512,3) , np.uint8)


	cv2.imshow('PIka', img)
	cv2.waitKey(0)
	cv2.destroyWindow('Pika')

if __name__ == "__main__":
    main()	
