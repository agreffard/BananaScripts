import pytumblr
import os
import codecs

client = pytumblr.TumblrRestClient(
  # fill with my tumblr authentication data
)

# very ugly code to automatically upload pictures to my tumblr blog - with date and caption
# nee pytumblr - https://github.com/tumblr/pytumblr

folder = "images"
textsFile = "texts.txt"
datesFile = "dates.txt"
nbImg = 42
offset = 0

dirList = os.listdir("./"+folder)
images = []
i = 0
for path in dirList:
    if os.path.isdir(path) == False:
        i = i+1
        images.append(folder+"/"+str(i)+".jpg")

with codecs.open(textsFile, "r", "utf-8") as f:
    texts = [line for line in f]

with codecs.open(datesFile, "r", "utf-8") as f:
    dates = [line for line in f]

for i in range(nbImg-offset):
    print dates[offset+i]
    response = client.create_photo('agreffard-nyc', state="published", data=images[offset+i], caption=texts[offset+i], date=dates[offset+i])
    print response
