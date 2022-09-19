from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser


def index(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get("q")
        db_tweets = Tweets()
        parser = Parser()
        tweets = db_tweets.get_tweets_about(query)
        if not tweets:
            tweets = parser.get_fr_tweets_about(query)
        context["tweets"] = tweets
        for tweet in tweets:
            db_tweets.insert(tweet)
        return render(request, "index.html", context=context)
    if request.method == "GET":
        return render(request, "index.html", context=context)
