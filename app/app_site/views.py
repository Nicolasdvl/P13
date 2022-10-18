from django.shortcuts import render
from twt_db.models import Tweets
from twt_api.parser import Parser
from django.views import View
import json


class Index(View):
    def __init__(self):
        self.context = {}
        self.db_tweets = Tweets()
        self.parser = Parser()

    def get(self, request):
        self.context["cloud_json"] = json.dumps(self.db_tweets.meta_query())
        return render(request, "index.html", context=self.context)

    def post(self, request):
        query = request.POST.get("q")
        # if doesn't exist in db
        if not Tweets.objects.filter(query=query).exists():
            temp = []
            # get tweets
            tweets = self.parser.get_fr_tweets_about(query)
            for tweet in tweets:
                self.db_tweets.insert(tweet, query)
                # get conversations
                if tweet.conversation_id not in temp:
                    if conversation := self.parser.get_conversation(
                        tweet.conversation_id
                    ):
                        temp.append(tweet.conversation_id)
                        for conversation_tweet in conversation:
                            self.db_tweets.insert(conversation_tweet, query)

        conversations = self.db_tweets.get_conversations_about(query)
        self.context["conversations_json"] = json.dumps(conversations)
        self.context["conversations"] = conversations
        return render(request, "index.html", context=self.context)
