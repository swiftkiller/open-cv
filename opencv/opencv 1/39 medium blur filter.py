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

	noisy = np.zeros(img.shape, np.uint8)

	for i in range(rows):
		for j in range(columns):
			r=rand.random()
			if r<p/2:  #pepper
				noisy[i][j]=[0,0,0]
			elif r<p:  #salt
				noisy[i][j]=[255,255,255]
			else:  #same
				noisy[i][j]=img[i][j]		

	denoised = cv2.medianBlur(noisy, 3)

	output = [img, noisy, denoised]
	titles = ['original', 'noisy', 'denoised']

	for i in range(3):
		plt.subplot(1,3,i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()


if __name__ == "__main__":
	main()	