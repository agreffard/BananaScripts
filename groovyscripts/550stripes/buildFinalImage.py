# Builds the main image containing all 550 images as color stripes
# 550 stripes = 550 colors = 550 images = 550 pictures from July 2016 to December 2017
# See https://agreffard.github.io/thecolorsofnewyorkcity/

import cv2
import numpy
import os
import struct

def picsUrl():
  num = 50
  start = 0
  url = "https://agreffard-nyc.tumblr.com/api/read?type=photo&num={}&start={}".format(num, start)

def int2hex(n):
  return format(int(n), '02x')

def rgb2hex(rgb):
  return "#" + "".join([int2hex(i) for i in rgb[::-1]])

def writeColor(file, color):
  hex = rgb2hex(color[0:3])
  file.write(hex + "\n")

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
nbTotalImages = sum(nbImgs.values())
print nbTotalImages

width = 5
height = 1400
final_image = numpy.zeros((height, nbTotalImages*width + width, 4), numpy.uint8)
main_mean_image = numpy.zeros((1, nbTotalImages, 4), numpy.uint8)
file_colors = open("colors.txt", "w") 

offset = 0
for folderIndex in xrange(nbFolders):
  folder = folderPath(folderIndex)
  print folder
  nbImg = nbImgs[folder]
  for i in range(nbImg):
    imgname = "{}/{}.jpg".format(folder, i+1)
    img = cv2.imread(imgname)
    # array = numpy.array(img)
    mean = cv2.mean(img)
    main_mean_image[0, offset] = mean
    print str(i)
    writeColor(file_colors, mean)
    for j in xrange((offset + i)*width, (offset + i+1)*width):
      for k in xrange(0, height):
        final_image[k][j] = mean
  offset += nbImg

file_colors.close()
cv2.imwrite("result_final.jpg", final_image)
cv2.destroyAllWindows()
