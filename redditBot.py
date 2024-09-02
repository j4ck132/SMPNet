import warnings
warnings.filterwarnings("ignore")

import praw
import responses
import time

reddit = praw.Reddit(client_id='rCZeqGE72pnYjhcKkvwSMA',
                     client_secret='JnnNx-1FU82WS3el8Ez-QVtVZS3kwg',
                     user_agent='<console:LONELY:1.0',
                     username = 'LonelyDetectorV1',
                     password = 'lonelylonely')

subreddit = reddit.subreddit("lonely")

for post in subreddit.new(limit=15):
    response = responses.handle_response(post.selftext)
    if (response != ""):
        print("**********")
        print(post.title)
        post.reply(response)
        time.sleep(60)