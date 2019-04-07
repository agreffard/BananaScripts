# Experimental code for time remap (anamorphose temporelle) from webcam using OpenCV
# Inspiration Adrien M & Claire B - https://vimeo.com/7878518

import cv2
import numpy as np
from time import gmtime, strftime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS , 60.0)

filename = 'output-{}.avi'.format(strftime("%Y-%m-%d-%H-M-%S", gmtime()))
print filename
out = cv2.VideoWriter(filename, -1, 60.0, (640,480))

#init
ret, frame = cap.read()
size = np.array(frame).shape
print str(size)
#print frame
height, width = size[0], size[1]

nb_cache = height/10
cache_images = np.zeros((height, height, width, 3), np.uint8)
cursor = -1

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:
        cursor = (cursor + 1) % height

        for current_line in range(height):
            index = (cursor + current_line) % height
            cache_images[index, current_line] = frame[current_line]

        img = cache_images[cursor]

        out.write(img)

        # Display the resulting frame
        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
