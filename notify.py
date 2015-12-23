#Enter the a timer remainder 
import re
import sys
import random

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
	'''
	def setId(id):
		self.__id = id
	'''
	def getMessage():
		return self.__message
	def setMessage(message):
		self.__message = message
def help():
	print "Notify is designed for you to type in a"
	print "quick remainder message and a remaninder time"
	print ""
	print "'new 'message' - creates notification and will ask you for remainder time"
	print "'delete id' - 	delete notification based on notification id"
	print "'list' -      	lists active notifications, time, id"
	print "'update id' - 	update time with this id"
	print "'help' -      	this page"

def error(command):
	print "unknown command: " + command

def list():
	for notif in active_notif:
		print "Notification id " + notif.getId
		print "Notification message " + notif.getMessage
		print "Notification time left " + notif.getTime
		
def delete(id):
	del active_notif[id]
	
def update(id):
	print "Notification: " + active_notif[id]
	time = input("New Time: Enter To Skip")
	message = input("New Message: Enter To Skip")
	if time != "":
		active_notif[id].setTime = time
	if message != "":
		active_notif[id].setMessage = message

def new(message):
	time = input("Notify me in:, HH:MM:SS format")
	id = random.random()
	while dict[id] != None:
		id = random.random()
		
	dict[id] = Notification(message, time, id)
	
#main
'''
print "YO! "+len(sys.argv)
print "list "+ str(sys.argv)
'''
if len(sys.argv) == 1:
	help()
command = sys.argv[1]
elif len(sys.argv) == 2:
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
	elif command == "new":
		new(second)
	else:
		error(command)
else:
	error(command)
	
