import cv2
import time

def main():
	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"
	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	img1 = cv2.imread(imgpath1, 1) 

	rows, columns, channels = img1.shape

	angle = 0

	while True:

		if angle == 360:
			angle = 0
		R = cv2.getRotationMatrix2D((columns/2,rows/2), angle, 0.25)
		print(R)

		output = cv2.warpAffine(img1, R, (columns, rows))

		cv2.imshow('Rotation Image', output)
		angle = angle +1
		time.sleep(0.01)

		if cv2.waitKey(1)==27:
			break

	cv2.destroyWindow('Rotated Image')

if __name__ == '__main__':
	main() 
