import cv2
import numpy as np

def main():

    cap=cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:

        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #blue colour
        low = np.array([100,50,50])
        high = np.array([140,255,255])

        image_mask = cv2.inRange(hsv, low, high)

        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow('Masking', image_mask)
        cv2.imshow('Qriginal Webcam Feed', frame)
        cv2.imshow('Colour Tracking', output)
        if cv2.waitKey(33)==27:
                break
        
    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()    
