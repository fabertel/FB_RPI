#!/usr/bin/python
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1862
#2016-09-18 .. aggiunto data in filename e upload in dropbox 
#v1 loop
#v1.3 - 2017/10/01
#	added library con visualizzazione per sleep 
#	removed photo from PI memory 
#	added stand and rotated photo
#v1.7 - 2017/10/01
#	added image comparison
#	removed foto from local 
#	email at startup 
#os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload FB_Log.txt /RPI_test2/");
#takes 100 foto una ogni 5minuti : 5 ore 

import os
import time
import subprocess
import datetime
import FB_LIB_01_EEMAIL as fb_eml

import numpy as np
from PIL import Image, ImageChops

image = Image.new('RGB', (640, 480), (255, 255, 255))
previousphotoname = "comparison.png"
image.save(previousphotoname, "PNG")
previousphoto = Image.open("comparison.png").convert('L')

vversion = 'v17'
fb_eml.EEMAIL('RPI Connected','Monitoring ON')
photo_counter = 0    # Photo counter
photo_new_counter = 0
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print "Starting photo" + vversion

while (photo_counter < 1000):

	timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S') 
	photo_counter = photo_counter + 1
	filename = vversion + '_' + str(timestamp) + '.jpg'
	makeaphoto = 'raspistill -o ' + filename + ' -w 640 -h 480 -rot 180 -t 1';
	pid = subprocess.call(makeaphoto, shell=True) 
	#print ("comparison fra" + filename + " e " + previousphotoname)
	im1 = Image.open(filename).convert('L')
	im2 = Image.open(previousphotoname).convert('L')
	diff = ImageChops.difference(im2,im1)
	diffdata = np.asarray( diff, dtype="int32" ) 

	if diffdata.sum()>3000000: 
		score = 'NEW '
		photo_new_counter = photo_new_counter +1 
		print(str(photo_counter) + '---' + str(photo_new_counter) + '---' + score + str(diffdata.sum()) + '---' + str(timestamp))
		print 'Uploading' + str(photo_counter) + '  ' + filename

		Uploader = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh "
		SourcePath = "/home/pi/FB/"
		UploadPath = "/RPI_test2/"
		ScriptUpload = Uploader+"upload "+SourcePath+filename+" "+UploadPath
		print (ScriptUpload)
		subprocess.call(ScriptUpload, shell=True)
		os.remove(previousphotoname)
		previousphotoname=filename
	else:
		score = 'OLD '
		print(str(photo_counter) + '---' + str(photo_new_counter) + '---' + score + str(diffdata.sum()) + '---' + str(timestamp))
		os.remove(filename)

	time.sleep(2)

print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print('END')
