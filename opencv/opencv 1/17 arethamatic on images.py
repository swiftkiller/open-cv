import cv2
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	imgpath2= path + "WIN_20190301_18_04_19_Pro.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	
	add = img1 + 50
	sub = img1 - img2
	mult = img1 * img2
	div = img1 / 5

	titles = ['Gyo', 'snoker','Add', 'sub','mult', 'div']
	images = [img1, img2, add, sub, mult, div] 

	for i in range(6):
		plt.subplot(1, 6, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
