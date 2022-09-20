from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser


def index(request):
    context = {}
    conversations = []
    if request.method == "POST":
        query = request.POST.get("q")
        db_tweets = Tweets()
        parser = Parser()
        tweets = db_tweets.get_tweets_about(query)
        if not tweets:
            tweets = parser.get_fr_tweets_about(query)
            for tweet in tweets:
                if conversation := parser.get_conversation(
                    tweet.conversation_id
                ):
                    conversations.append(conversation)

        else:
            conversations.extend(
                db_tweets.get_conversation(tweet.conversation_id)
                for tweet in tweets
            )

        context["tweets"] = tweets
        context["conversations"] = conversations
        for tweet in tweets:
            db_tweets.insert(tweet)
        return render(request, "index.html", context=context)
    if request.method == "GET":
        return render(request, "index.html", context=context)
