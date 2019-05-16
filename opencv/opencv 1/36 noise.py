import cv2
import matplotlib.pyplot as plt
import numpy as np
import random as rand

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	imgpath1 = path + 'lena_color_512.tif'
	img = cv2.imread(imgpath1, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	rows, columns,  channels = img.shape
	p= 0.05

	output = np.zeros(img.shape, np.uint8)



	for i in range(rows):
		for j in range(columns):
			r=rand.random()
			if r<p/2:  #pepper
				output[i][j]=[0,0,0]
			elif r<p:  #salt
				output[i][j]=[255,255,255]
			else:  #same
				output[i][j]=img[i][j]		


	plt.imshow(output)
	plt.title('salt and pepper noise')
	plt.show()


if __name__ == "__main__":
	main()	