#!/usr/bin/python3.5

import psutil
import os
import time
import threading
import daemon

def apalah():
	try:
		os.system("zenity --info --text 'Battery monitor, started - Kevin Agusto'")
	except:
		x = 10
threading.Thread(target=apalah).start()

def pesan():
				try:
					os.system("zenity --error --text 'Warning System Low Battery. shutdown in 30 seconds' - Kevin Agusto -")
				except:
					pass
if True:
	while True:
		x = (str(psutil.sensors_battery().percent))
		x = x[0:list(x).index(".")]
		if int(x) <= 3:
				threading.Thread(target=pesan, args=[]).start()
				time.sleep(30)
				try:
					with open("/root/baterai.log", "w+") as writer:
						writer.write("otomatis mati pada %s" %(str(time.ctime())))
				except:
					pass
				try:
					os.system("poweroff")
				except:
					pass
				os.system("poweroff")
		time.sleep(3)
