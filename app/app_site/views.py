from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser


def index(request):
    context = {}
    conversations = {}
    if request.method == "POST":
        query = request.POST.get("q")
        db_tweets = Tweets()
        parser = Parser()
        # if exist in db
        if Tweets.objects.filter(query=query).exists():
            conversations = db_tweets.get_conversations_about(query)

        # else call api
        else:
            # get tweets
            tweets = parser.get_fr_tweets_about(query)
            # get conversations
            for tweet in tweets:
                if tweet.conversation_id not in conversations:
                    if conversation := parser.get_conversation(
                        tweet.conversation_id
                    ):
                        conversations[tweet.conversation_id] = conversation
                    else:
                        conversations[tweet.conversation_id] = [tweet]

            # insert in db
            for key, conversation in conversations.items():
                for conversation_tweet in conversation:
                    db_tweets.insert(conversation_tweet, query)

        context["conversations"] = conversations
        return render(request, "index.html", context=context)

    if request.method == "GET":
        return render(request, "index.html", context=context)
