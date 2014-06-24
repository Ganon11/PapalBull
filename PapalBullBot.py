import os
import praw
import re
import time

USERNAME = "Papal_Bull"
PASSWORD_FILEPATH = os.path.join(os.getcwd(), 'files', 'password.dat')
COMMENT_PATTERN = re.compile(r'http://www.reddit.com/r/(?P<subreddit>\w+)/comments/(?P<thread_id>\w+)/\w+/(?P<comment_id>\w+)', re.IGNORECASE)
ALLOWED_SUBREDDITS = (
   'Christianity',
   'Sidehugs'
)
PAPAL_BULL_MESSAGE = "[papal bull](http://imgur.com/dZBlaTj.gif)"

def GetPassword():
   password = ''
   PASSWORD_FILE = open(PASSWORD_FILEPATH)
   password = PASSWORD_FILE.read()
   PASSWORD_FILE.close()
   return password

user_agent = ("Papal Bull Bot Account by /u/Ganon11 github.com/Ganon11/PapalBull")
password = GetPassword()

def CheckMessages():
   r = praw.Reddit(user_agent=user_agent)
   r.login(USERNAME, password)

   for msg in r.get_unread(limit=None):
      m = re.match(COMMENT_PATTERN, msg.body)
      if m is not None:
         msg.mark_as_read()
         whole_url = m.group(0)
         sub = m.group('subreddit')
         if sub in ALLOWED_SUBREDDITS:
            comment = r.get_submission(whole_url).comments[0]
            comment.reply(PAPAL_BULL_MESSAGE)
      else:
         msg.mark_as_read()

while True:
   CheckMessages()
   time.sleep(600) # Sleep for 10 minutes before checking again.