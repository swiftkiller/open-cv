import cv2
import numpy as np 

def main():
    windowName='Live Video'
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        print(frame)   
    else:
        ret = False

    while ret:
        ret, frame = cap.read()

        (b,g,r) = cv2.split(frame)

        M = np.maximum(np.maximum(r,g),b)
        r[r<M] = 0
        g[g<M] = 0
        b[b<M] = 0

        output = cv2.merge((b,g,r))

        cv2.imshow(windowName, output)
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyWindow(windowName)

    cap.release()

if __name__=="__main__":
    main()    

