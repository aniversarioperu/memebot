import unittest

from memebot.twitter import search_in_twitter


class TestTwitter(unittest.TestCase):
    def setUp(self):
        pass

    def test_search_in_twitter(self):
        keywords = 'cucaracha domino'
        expected = [
            {
                'tweet_id': '564588665536774144',
                'retweet_count': 13,
                'status': 'Esta es la Cucaracha Dominó. No es broma, así se llama. http://t.co/8InBGOkITl',
                'screen_name': 'eldiarionegro',
                'image_urls': ['http://pbs.twimg.com/media/B9XSFARIEAA1DBJ.jpg'],
            },
        ]
        result = search_in_twitter(keywords)
        self.assertEqual(expected, result)
