import cv2
import matplotlib.pyplot as plt


def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	img = cv2.imread(imgpath1, 1)
	img1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR )

	r,g,b = cv2.split(img1)

	titles = ['Original Immage', 'Red', 'Green', 'Blue']
	images = [cv2.merge((r,g,b)), r, g, b]

	plt.subplot(2,4,1)
	plt.imshow(images[0])
	plt.title(titles[0])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,2)
	plt.imshow(images[1], cmap='gray')
	plt.title(titles[1])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,3)
	plt.imshow(images[2],cmap='gray')
	plt.title(titles[2])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,4)
	plt.imshow(images[3], cmap='gray')
	plt.title(titles[3])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,5)
	plt.imshow(images[1], cmap='Reds')
	plt.title(titles[1])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,6)
	plt.imshow(images[2],cmap='Greens')
	plt.title(titles[2])
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2,4,7)
	plt.imshow(images[3], cmap='Blues')
	plt.title(titles[3])
	plt.xticks([])
	plt.yticks([])

	plt.show()

if __name__ == '__main__':
	main()	