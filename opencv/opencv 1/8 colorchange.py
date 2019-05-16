import cv2
import matplotlib.pyplot as plt

def main():
    imgpath =  "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\WIN_20170902_18_09_13_Pro.jpg"
    img = cv2.imread(imgpath, 1)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.title('original')
    plt.xticks([])
    plt.yticks([])
    plt.show()



if __name__=="__main__":
    main()    
