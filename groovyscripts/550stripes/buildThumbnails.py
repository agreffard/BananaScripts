# Builds a thumbnail for each image
# Used for https://agreffard.github.io/thecolorsofnewyorkcity

import cv2
import numpy
import os
import struct

def nbImgInFolder(folder):
  return len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])

def nbImginFolders(nbFolders):
  nbImgs= {}
  for folderIndex in xrange(nbFolders):
    folder = folderPath(folderIndex)
    nbImgs[folder] = nbImgInFolder(folder)
  return nbImgs

def folderPath(index):
  return "./images/images" + str(index+1)

nbFolders = 9
nbImgs= nbImginFolders(nbFolders)

def resize(minSize):
  for folderIndex in xrange(nbFolders):
    folder = folderPath(folderIndex)
    print folder
    nbImg = nbImgs[folder]
    for i in range(nbImg):
      imgname = "{}/{}.jpg".format(folder, i+1)
      img = cv2.imread(imgname)
      height, width = img.shape[:2]
      portract = height > width
      if portract:
        newWidth = minSize
        newHeight = minSize * height / width
      else:
        newHeight = minSize
        newWidth = minSize * width / height
      newSize = (newWidth, newHeight)
      resizedImage = cv2.resize(img, newSize)
      if not os.path.exists("./thumbnails"+folder[1:]):
        os.makedirs("./thumbnails"+folder[1:])
      cv2.imwrite("./thumbnails"+imgname[1:], resizedImage)

resize(100)
