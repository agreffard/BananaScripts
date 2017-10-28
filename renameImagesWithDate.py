# rename all images in current directory by adding the date before the original file name
import os
from datetime import datetime
for filename in os.listdir("."):
	if filename.startswith("IMG_"):
		time = os.path.getmtime(filename)
		prefix = datetime.fromtimestamp(time).strftime('%Y %m %d_')
		newName = prefix + filename
		os.rename(filename, newName)
