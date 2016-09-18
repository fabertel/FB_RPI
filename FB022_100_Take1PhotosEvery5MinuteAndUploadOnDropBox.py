#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1862
#2016-09-18 .. aggiunto data in filename e upload in dropbox 
#v1 loop
#takes 100 foto una ogni 5minuti : 5 ore 

import os
import time
import subprocess
import datetime

photo_counter = 0    # Photo counter
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print "Starting photo"

timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S') 

while (photo_counter < 100):

	photo_counter = photo_counter + 1
	filename = 'photo_' + str(timestamp) + '.jpg'
	#filename = 'photo_' + str(photo_counter) + '.jpg'
	
	print filename
	print photo_counter
	makeaphoto = 'raspistill -o ' + filename + ' -w 640 -h 480 -t 1';
	pid = subprocess.call(makeaphoto, shell=True) 
	#subprocess.call(makeaphoto, shell=True) 
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
	print ("foto effettuata")  

	#upload in dropbox 
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
	#filename2 = "photo_20160918_140444.jpg";
	print('Uploading')
	Uploader = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh "
	SourcePath = "/home/pi/FB/"
	UploadPath = "/RPI_test2/"
	ScriptUpload = Uploader+"upload "+SourcePath+filename+" "+UploadPath
	print (ScriptUpload)
	subprocess.call(ScriptUpload, shell=True)
	
	time.sleep(300)

#os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload FB_Log.txt /RPI_test2/");

print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
print('END')