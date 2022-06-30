
import pyinotify
import os
import sys





bin_dir = "/app"
print(bin_dir)


wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CREATE  # watched events


import time 
class EventHandler(pyinotify.ProcessEvent):
	def process_IN_CREATE(self, event):
	
	    bin_fname = os.path.split((event.pathname))[1]
	    file_full_path = bin_dir + "/" + bin_fname
	    
	    print("gelen dosyanın adı:",bin_fname)
	    
	    with open(file_full_path) as f:
    		lines = f.readlines()
    		print("Dosyanın içeriği")
    		print(lines)
	    time.sleep(.2)
	    
	    
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(bin_dir, mask, rec=True)

notifier.loop()


