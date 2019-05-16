import cv2

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\4.1.08.tiff"

img=cv2.imread(imgpath,cv2.IMREAD_COLOR)
output= "C:\\Users\\spars\\OneDrive\\Pictures\\set\\pika.tiff"

car = img[80:100,55:73]

img[40:60, 30:48]=car

cv2.imshow('Pika', car)

cv2.imwrite(output, car)

cv2.waitKey(0)
cv2.destroyWindow('Pika')

