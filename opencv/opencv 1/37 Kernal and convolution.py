import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	imgpath1 = path + '4.2.07.tiff'
	img = cv2.imread(imgpath1, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	k= np.array(([-1,-1,-1],[-1,7,-1],[-1,-1,-1]),np.float32)
	print(k)

	output = cv2.filter2D(img,-1,k)

	plt.subplot(1,2,1)
	plt.imshow(img)
	plt.title('Original Image')

	plt.subplot(1,2,2)
	plt.imshow(output)
	plt.title('Filtered image')

	plt.show()

if __name__ == "__main__":
	main()		
