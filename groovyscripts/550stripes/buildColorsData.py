# Builds a json file containing data for each stripe (image, text, main color)
# Used for https://agreffard.github.io/thecolorsofnewyorkcity

import json
import os
import codecs

def nbImgInFolder(index):
  folder = "./images/images" + str(index+1)
  return len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])

def getLines(fileName):
  lines = codecs.open(fileName, "r", "utf-8").readlines()
  return [line.rstrip('\r\n') for line in lines]

nbFolders = 9
colors = getLines("colors.txt")
stripes = []

imageIndexGlobal = 0
for folderIndex in xrange(nbFolders):
  nbImgs = nbImgInFolder(folderIndex)
  for imageIndex in range(nbImgs):
    print imageIndex
    imageName = "images/images{}/{}.jpg".format(folderIndex + 1, imageIndex + 1)
    texts = getLines("texts/texts{}.txt".format(folderIndex + 1))
    stripe = {
      "id": imageIndexGlobal,
      "text": texts[imageIndex],
      "image": imageName,
      "color": colors[imageIndexGlobal]
    }
    print texts[imageIndex]
    stripes.append(stripe)
    imageIndexGlobal = imageIndexGlobal + 1

with open('stripes.json', 'w') as stripesFile:
  json.dump(stripes, stripesFile)
