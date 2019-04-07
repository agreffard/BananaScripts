# Generates fireworks of multiple series of disco balls of random colors
# Extremely experimental (beginning of) project

import numpy as np
import cv2
from random import randint

sizeImg = 1024
nbCircles = randint(0, 250)
maxFrames = randint(1, 60)

def rand():
    return randint(0, sizeImg-1)

def randcol():
    return randint(0, 255)

centers = [(rand(), rand()) for a in range(nbCircles)]
colors = [(randcol(), randcol(), randcol()) for b in range(nbCircles)]
frames = [randint(0, 50) for c in range(nbCircles)]
factors = [randint(1, 3) for d in range(nbCircles)]

i = 0
while(True):
    i = i % maxFrames
    img = np.zeros((sizeImg,sizeImg,3), np.uint8)

    for n in range(nbCircles):
    	print factors[n]
        cv2.circle(img,centers[n], (frames[n] + i % maxFrames) * factors[n], colors[n], -1)
    
    cv2.imshow('DISCOOOOO!', img)
    
    if i == 0:
        maxFrames = randint(0, 60)
        nbCircles = randint(0, 150)
        centers = [(rand(), rand()) for a in range(nbCircles)]
        colors = [(randcol(), randcol(), randcol()) for b in range(nbCircles)]
        frames = [randint(0, 50) for c in range(nbCircles)]
        factors = [randint(1, 3) for d in range(nbCircles)]


    i=i+1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
