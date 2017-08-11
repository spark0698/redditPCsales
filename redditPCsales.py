#!/usr/bin/env python2

import praw
import time

r = praw.Reddit()

def run_bot():
    subreddit = r.subreddit("test")

    for submission in subreddit.stream.submissions():
        r.redditor("eatdatrice16").message("test", submission)

while True:
    run_bot()
    time.sleep(10)