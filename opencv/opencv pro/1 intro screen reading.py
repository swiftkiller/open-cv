import cv2
import numpy as np 
from PIL import ImageGrab
import time

last_time =time.time()

while(True):
	screen = np.array(ImageGrab.grab(bbox = (0,0,600,720)))
	screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
	#printscreen_numpy = np.array(printscreen_pil.getdata(),dtype = 'uint8')\
	#.reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

	print('loop took {}seconds '.format(time.time()-last_time))
	last_time = time.time()
	cv2.imshow('window',screen)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break 