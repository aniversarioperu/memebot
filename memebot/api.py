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
        self.memes = []

    def find_memes(self, keywords):
        memes = twitter.search_in_twitter(keywords)
        print(memes)