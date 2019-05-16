import cv2

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\WIN_20170902_18_09_13_Pro.jpg"

img=cv2.imread(imgpath , 0)

print(img)


print(type(img))
print(img.dtype)
print(img.shape)
print(img.ndim)
print(img.size)


cv2.imshow('PIka', img)
#cv2.waitKey(0)
#cv2.destroyWindow('Pika')
