import cv2
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "5.1.11.tiff"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	Laplacian = cv2.Laplacian(img, -1, ksize=3, scale=1, delta=0, borderType = cv2.BORDER_DEFAULT)
	
	sobelx = cv2.Sobel(img, -1, dx=2,dy=0,ksize = 11, scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	sobely = cv2.Sobel(img, -1, dx=0,dy=2,ksize = 11, scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	sobel = sobelx + sobely

	scharrx = cv2.Scharr(img, -1, dx=1,dy=0,scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	scharry = cv2.Scharr(img, -1, dx=0,dy=1,scale=1,delta=0, borderType= cv2.BORDER_DEFAULT)
	scharr = scharrx + scharry

	titles = ['original','Laplacian','original','sobelx', 'sobely','sobel','scharrx','scharry','scharr']
	output = [img, Laplacian, img, sobelx, sobely, sobel, scharrx, scharry, scharr] 

	for i in range(9):
		plt.subplot(3, 3, i+1)
		plt.imshow(output[i],cmap ='gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
