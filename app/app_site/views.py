from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser


def index(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get("q")
        tweets = Tweets()
        parser = Parser()
        tweets = tweets.get_tweets_about(query)
        if not tweets:
            tweets = parser.get_fr_tweets_about(query)
        context["tweets"] = tweets
        return render(request, "index.html", context=context)
    if request.method == "GET":
        return render(request, "index.html", context=context)
