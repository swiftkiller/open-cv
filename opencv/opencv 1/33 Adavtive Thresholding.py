import cv2
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	#imgpath1 = path + "gray21.512.tiff"
	imgpath1 = path + "4.1.05.tiff"
	#imgpath1 = path + "5.1.09.tiff"
	#imgpath1 = path + "cameraman.tif"

	img = cv2.imread(imgpath1, 0)

	bock_size = 101
	constant = 2
	th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, bock_size, constant)
	th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bock_size, constant)


	output = [img, th1, th2]
	titles = ['Original', 'ADAPTIVE_MEAN', 'ADAPTIVE_GAUSSIAN']

	for i in range(3):
		plt.subplot(1, 3, i+1)
		plt.imshow(output[i],cmap = 'gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
