import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	img1 = cv2.imread(imgpath1, 1) 
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

	rows, columns, channels = img1.shape

	t=np.float32([[1,5,50],[0,1,-50]])
	print(t)

	output = cv2.warpAffine(img1, t, (columns, rows))


	plt.imshow(output)
	plt.title('Shifted Image')
	plt.show()

if __name__ == '__main__':
	main() 	
