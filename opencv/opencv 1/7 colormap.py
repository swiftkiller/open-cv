import cv2
import matplotlib.pyplot as plt

def main():
    imgpath =  "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\WIN_20170902_18_09_13_Pro.jpg"
    img = cv2.imread(imgpath, 0)

    plt.imshow(img,cmap = 'gray')
    plt.title('Gray Colormap')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    plt.imshow(img, cmap = 'Accent')
    plt.show()

if __name__=="__main__":
    main()
