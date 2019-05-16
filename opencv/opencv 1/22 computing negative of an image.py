import cv2
import matplotlib.pyplot as plt


def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	img = cv2.imread(imgpath1, 1)
	
	img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img3 = abs(255-img1)
	img4 = abs(255-img2)

	r,g,b = cv2.split(img1)

	titles = ['Original Immage', 'grayscale', 'Colour nagative', 'grayscalenegative']	
	images = [img1, img2, img3, img4]

	plt.subplot(2,2,1)
	plt.imshow(images[0])
	plt.title(titles[0])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,2,2)
	plt.imshow(images[1], cmap='gray')
	plt.title(titles[1])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,2,3)
	plt.imshow(images[2])
	plt.title(titles[2])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,2,4)
	plt.imshow(images[3], cmap='gray')
	plt.title(titles[3])
	plt.xticks([])
	plt.yticks([])


	plt.show()

if __name__ == '__main__':
	main()	