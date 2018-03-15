#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import thread
import time
import threading


cmdEnterApp = "adb shell am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n com.myos.camera/com.myos.camera.activity.CameraActivity"
#keyevent 25 as volumn key; keyevent 3 as home key.
cmdTakePic = "adb shell input keyevent 25"
cmdGoHome = "adb shell input keyevent 3"


class myThread (threading.Thread):   #继承父类threading.Thread
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
		print "Starting " + self.name
		#print_time(self.name, self.counter, 5)
		if self.threadID == 1:
			enter_app_then_capture(self.name)
		else:
			go_back_home(self.name)
		print "Exiting " + self.name


def enter_app_then_capture(threadName):
	os.system(cmdEnterApp)
	time.sleep(1)
	os.system(cmdTakePic)
	print threadName, ": just take picture."

def go_back_home(threadName):
	time.sleep(2)
	print threadName, ": will go home now."
	os.system(cmdGoHome)
	
def main():
	while True:
		try:
			# 创建新线程
			print "start to do sth."
			thread1 = myThread(1, "Thread-1", 1)
			thread2 = myThread(2, "Thread-2", 2)
			
			# 开启线程
			thread1.start()
			thread2.start()
		except:
			print "Error: unable to start thread."
			
		time.sleep(4)


if __name__ == '__main__':
	main()