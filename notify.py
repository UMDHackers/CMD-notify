#Enter the a timer remainder 
import thread
import re
import sys
import random
from time import gmtime, strftime
import time

#Global
active_notif = dict()

class Notification:
	def __init__(self, message, time, id):
		self.__message = message
		self.__time = time
		self.__id = id
	def getTime():
		return self.__time
	def setTime(time):
		self.__time = time
	def getId():
		return self.__id
	def getMessage():
		return self.__message
	def setMessage(message):
		self.__message = message
def help():
	print "Notify is designed for you to type in a"
	print "quick remainder message and a remaninder time"
	print ""
	print "'new 'message' HH:MM:SS' - creates notification for time, please have quotes around the message"
	print "'delete id' - 			 delete notification based on notification id"
	print "'list' -      			 lists active notifications, time, id"
	print "'update id' - 			 update time with this id"
	print "'help' -      			 this page"

def error(command):
	print "unknown command: " + command

def list_info():
	for notif in active_notif:
		print "Notification id " + notif.getId
		print "Notification message " + notif.getMessage
		print "Notification me at " + notif.getTime
		
def delete(id):
	if dict[id] is not None:
		del active_notif[id]
	else:
		print "That notification does not exist"
def update(id):
	if dict[id] is not None:
		print "Notification: " + active_notif[id]
		time = raw_input("Notif me in (HH:MM:SS): Enter To Skip")
		message = raw_input("New Message: Enter To Skip")
		if time != "":
			time = create_time(time)
			active_notif[id].setTime = time
		if message != "":
			active_notif[id].setMessage = message
	else:
		print "That notification does not exist"
def new(string_notif):
	list_string = string_notif.split("_")
	message = list_string[0]
	time = list_string[1]
	time = create_time(time)
	id = (random.random() * 10000)/13
	print "id " + str(id)
	while str(id) in active_notif:
		id = (random.random() * 10000)/13
	active_notif[str(id)] = Notification(message, time, id)

def create_time(timer):
	#pasre the time given
	current = strftime("%H:%M:%S", time.localtime())
	time_array = timer.split(":")
	current = current.split(":")
	hours = int(current[0]) + int(time_array[0])
	mintues = int(current[1]) + int(time_array[1])
	seconds = int(current[2]) + int(time_array[2])
	add_mins = add_hours = days = 0
	if seconds >= 60:
		add_mins = seconds/60
		mintues = mintues + add_mins
	elif mintues >= 60:
		add_hours = mintues/60
		hours = hours + add_hours
	seconds = seconds%60
	mintues = mintues%60
	hours = hours%24
	string_time = str(hours) + ":" + str(mintues) + ":" + str(seconds)
	return string_time

	
def check():
	current = strftime("%H:%M:%S", time.localtime())
	for notfi in active_notif:
		if current == notfi.getTime:
			#Pop-up should go here 
			print notfi.getMessage
			delete(notfi.getId)


if len(sys.argv) == 1:
	help()

command = sys.argv[1]	
if len(sys.argv) == 2:
	
	if command == "help":
		help()
	elif command == "list":
		list_info()
	else:
		error(command)
elif len(sys.argv) == 3:
	second = sys.argv[2] 
	if command == "delete":
		delete(second)
	elif command == "update":
		update_notfi(second)
	else:
		error(command)
elif len(sys.argv) == 4:
	second = sys.argv[2]
	thrid = sys.argv[3]
	print "thrid " + thrid
	print "second " + second
	
	if command == "new":
		new(second + "_" + thrid)
	
else:
	command = sys.argv[1]
	error(command)
	

