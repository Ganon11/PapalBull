import os
import praw
import re
import time

USERNAME = "Papal_Bull"
PASSWORD_FILEPATH = os.path.join(os.getcwd(), 'files', 'password.dat')
COMMENT_PATTERN = re.compile(r'^http://www.reddit.com/r/(?P<subreddit>\w+)/comments/\w+/\w+/\w+$', re.IGNORECASE)
THREAD_PATTERN = COMMENT_PATTERN = re.compile(r'^http://www.reddit.com/r/(?P<subreddit>\w+)/comments/\w+/\w+$', re.IGNORECASE)
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
      m2 = re.match(THREAD_PATTERN, msg.body)
      msg.mark_as_read()
      if m is not None:
         whole_url = m.group(0)
         sub = m.group('subreddit')
         if sub in ALLOWED_SUBREDDITS:
            r.get_submission(whole_url).comments[0].reply(PAPAL_BULL_MESSAGE)
      elif m2 is not None:
         whole_url = m2.group(0)
         sub = m2.group('subreddit')
         if sub in ALLOWED_SUBREDDITS:
            r.get_submission(whole_url).add_comment(PAPAL_BULL_MESSAGE)

while True:
   CheckMessages()
   time.sleep(600) # Sleep for 10 minutes before checking again.
