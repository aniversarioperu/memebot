=====
Usage
=====


    >>> from memebot import Bot
    >>> bot = Bot()
    >>> keywords = 'cucaracha domino'
    >>> bot.find_memes(keywords)
    >>> len(bot.memes)
    50
    >>> bot.cluster_memes()
    >>> len(bot.clusters)
    5
    >>> bot.generate_html()
