import os
import praw
import random
import re
import time

USERNAME = "Papal_Bull"
PASSWORD_FILEPATH = os.path.join(os.getcwd(), 'files', 'password.dat')
COMMENT_PATTERN = re.compile(r'^http(?:s)?://www.reddit.com/r/(?P<subreddit>\w+)/comments/\w+/\w+/\w+$', re.IGNORECASE)
THREAD_PATTERN = re.compile(r'^http(?:s)?://www.reddit.com/r/(?P<subreddit>\w+)/comments/\w+/\w+/$', re.IGNORECASE)
ALLOWED_SUBREDDITS = (
   'Christianity',
   'Sidehugs'
)
COMMENT_MESSAGE = "What this comment needs is a nice, old fashioned, [papal bull](%s)."
THREAD_MESSAGE = "What this thread needs is a nice, old fashioned, [papal bull](%s)."
USER_AGENT = ("Papal Bull Account by /u/Ganon11 github.com/Ganon11/PapalBull")
BULLS = [
   "http://imgur.com/dZBlaTj.gif",
   "http://i.imgur.com/yEfaO0C.png",
   "http://fc07.deviantart.net/fs70/i/2013/053/b/1/papal_bull_by_poundcakery-d5vtv5v.jpg"
]

def GetPassword():
   PASSWORD_FILE = open(PASSWORD_FILEPATH)
   password = PASSWORD_FILE.read()
   PASSWORD_FILE.close()
   return password

def CheckMessages():
   password = GetPassword()
   r = praw.Reddit(user_agent=USER_AGENT)
   r.login(USERNAME, password)

   for msg in r.get_unread(limit=None):
      print "%s - read message \"%s\"" % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), msg.body)
      m = re.match(COMMENT_PATTERN, msg.body)
      m2 = re.match(THREAD_PATTERN, msg.body)
      if m is not None:
         whole_url = m.group(0)
         sub = m.group('subreddit')
         if sub in ALLOWED_SUBREDDITS:
            r.get_submission(whole_url).comments[0].reply(COMMENT_MESSAGE % random.choice(BULLS))
      elif m2 is not None:
         whole_url = m2.group(0)
         sub = m2.group('subreddit')
         if sub in ALLOWED_SUBREDDITS:
            r.get_submission(whole_url).add_comment(THREAD_MESSAGE % random.choice(BULLS))

      msg.mark_as_read()

def DoLoop():
   while True:
      CheckMessages()
      time.sleep(300) # Sleep for 5 minutes before checking again.

if __name__ == '__main__':
   DoLoop()
