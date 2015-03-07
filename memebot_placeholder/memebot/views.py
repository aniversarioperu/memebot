from django.shortcuts import render

from .api import Bot


def index(request):
    context = {'hola': 'que hace'}
    return render(request, 'memebot/index.html', context)


def search(request):
    query = request.POST['q']
    print(query)

    bot = Bot()
    bot.find_memes(query)
    bot.extract_ids()
    embeded_tweets = bot.get_embeded_tweets()
    context = {'embeded_tweets': embeded_tweets}
    return render(request, 'memebot/index.html', context)
