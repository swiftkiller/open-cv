import  numpy as np
from PIL import ImageGrab
import cv2
import time

def process_image(original_image):
    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    processed_img = cv2.Canny(processed_img , threshold1 = 200 , threshold2 = 300)
    return processed_img

def screen_record():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox = (100,40,1400,720)))
        new_screen = process_image(screen)
        cv2.imshow('window',new_screen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        #cv2.imshow('window',cv2.cvtColor(printscreen,cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
