# Extremely experimental project.
# First attempt at recreating the "OK GO - WTF?" effet without green screen (using only background extraction).
# https://www.youtube.com/watch?v=12zJw9varYE
# To be continued.

import cv2
import numpy as np
from time import gmtime, strftime

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
size = np.array(frame).shape
print size
height, width = size[0], size[1]

filename = 'output/okgo-{}.avi'.format(strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
out = cv2.VideoWriter(filename, -1, 30.0, (width,height))

nbImgInit = 0
threshold = 20
idx = -1
  
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        if idx < nbImgInit:
            idx = idx+1
            print idx
            continue

        if idx == nbImgInit:
            idx = idx+1
            background = frame
            img = background.copy()
            out.write(img)
            cv2.imshow('frame', img)
            continue

        # extract background
        mask = cv2.cvtColor(cv2.subtract(background, frame), cv2.COLOR_RGB2GRAY)

        for i in range(height):
            for j in range(width):
                if mask[i][j] >= threshold:
                    img[i][j] = frame[i][j]


        out.write(img)
        cv2.imshow('frame',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
