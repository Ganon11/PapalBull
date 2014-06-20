import os
import praw
import time

user_name = "PapalBull"
password_filepath = os.path.join(os.getcwd(), 'files', 'password.dat')

def GetPassword():
	password = ''
	PASSWORD_FILE = open(password_filepath)
	password = PASSWORD_FILE.read()
	PASSWORD_FILE.close()
	return password

user_agent = ("Papal Bull Bot Account by /u/Ganon11 github.com/Ganon11/PapalBull")
password = GetPassword()

r = praw.Reddit(user_agent=user_agent)
#r.login(user_name, password)
print "username: %(uname)s password: %(pw)s" % { 'uname': user_name, 'pw': password }
already_done = []

while True:
	time.sleep(600) # Sleep for 10 minutes before checking again.