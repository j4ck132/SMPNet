import warnings
warnings.filterwarnings("ignore")

import praw
import responses
import time

reddit = praw.Reddit(client_id='-----',
                     client_secret='-----',
                     user_agent='-----',
                     username = '-----',
                     password = '-----')

subreddit = reddit.subreddit("lonely")

for post in subreddit.new(limit=15):
    response = responses.handle_response(post.selftext)
    if (response != ""):
        print("**********")
        print(post.title)
        post.reply(response)
        time.sleep(60)
