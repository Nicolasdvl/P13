from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser
from django.views import View
import json


class Index(View):
    def __init__(self):
        self.context = {}

    def get(self, request):
        query_tags = Tweets.objects.values_list("query", flat=True).distinct()
        cloud_tag_data = {
            tag: Tweets.objects.filter(query=tag).count() for tag in query_tags
        }

        self.context["cloud_json"] = json.dumps(cloud_tag_data)
        return render(request, "index.html", context=self.context)

    def post(self, request):

        query = request.POST.get("q")
        db_tweets = Tweets()
        parser = Parser()
        # if doesn't exist in db
        if not Tweets.objects.filter(query=query).exists():
            temp = []
            # get tweets
            tweets = parser.get_fr_tweets_about(query)
            for tweet in tweets:
                db_tweets.insert(tweet, query)
                # get conversations
                if tweet.conversation_id not in temp:
                    if conversation := parser.get_conversation(
                        tweet.conversation_id
                    ):
                        temp.append(tweet.conversation_id)
                        for conversation_tweet in conversation:
                            db_tweets.insert(conversation_tweet, query)

        conversations = db_tweets.get_conversations_about(query)
        self.context["conversations_json"] = json.dumps(conversations)
        self.context["conversations"] = conversations
        return render(request, "index.html", context=self.context)
