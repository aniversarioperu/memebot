import requests

from . import twitter


class Bot(object):
    """
    Main class for memebot, only point of entry for users.

    Attr:
        * memes: list of dictionaries.
                 {'tweet_id': '', 'image_url': ['path'], 'status': 'text',
                  'screen_name': '', }
    """
    def __init__(self):
        self.memes = None
        self.tweet_ids = None

    def find_memes(self, keywords):
        self.memes = twitter.search_in_twitter(keywords)

    def extract_ids(self):
        ids = []
        for tweet in self.memes:
            ids.append(tweet['tweet_id'])
        self.tweet_ids = ids

    def get_embeded_tweets(self):
        embeded_tweets = []
        oauth = twitter.get_oauth()
        for id in self.tweet_ids:
            url = 'https://api.twitter.com/1.1/statuses/oembed.json'
            payload = {
                'id': id,
            }
            r = requests.get(url=url, auth=oauth, params=payload)
            r = r.json()
            tweet = r['html']
            embeded_tweets.append(tweet)
        return embeded_tweets
