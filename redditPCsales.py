#!/usr/bin/env python3

import praw
import time

c = open("yas.txt", "r")
creds = c.read().splitlines()

r = praw.Reddit(client_id = creds[0],
                client_secret = creds[1],
                username = creds[2],
                password = creds[3],
                user_agent = creds[4])

c.close()

def run_bot():
    subreddit = r.subreddit("test")

    for submission in subreddit.stream.submissions():
        r.redditor("eatdatrice16").message("test", submission)

while True:
    run_bot()
    time.sleep(10)