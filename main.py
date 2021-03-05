import requests
from flask import Flask, render_template, request
from scrapper import redit_scrapper
"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

db_reddits={}

app = Flask("DayEleven")
@app.route('/')
def home():
    return render_template("home.html",subreddits = subreddits)
@app.route('/read')
def read():
    reddits = {}
    reddits_key=[]
    for subreddit in subreddits:
        if request.args.get(subreddit):
            reddits_key.append(subreddit)
            db_exist = db_reddits.get(subreddit)
            if db_exist:
                pass
            else:
                url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
                posts = redit_scrapper(url)
                # reddits[subreddit] = {
                #     'posts':posts
                # }
                db_reddits[subreddit] = {
                    'posts':posts
                }
                # print(redit_scrapped)
    return render_template("read.html",db_reddits = db_reddits, reddits_key = reddits_key)
app.run(host="127.0.0.1",debug=True)