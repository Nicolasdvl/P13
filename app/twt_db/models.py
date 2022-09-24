from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet


class TwitterUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=280)

    def __str__(self):
        return str(self.id)


class Tweets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author_id = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    lang = models.CharField(max_length=2)
    created_at = models.DateTimeField()
    saved_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    public_metrics = models.CharField(max_length=500)
    referenced_tweets_id = models.BigIntegerField(null=True)
    referenced_tweets_type = models.CharField(max_length=280, null=True)
    conversation_id = models.BigIntegerField(default=0)
    in_reply_to_user_id = models.BigIntegerField(default=0)
    source = models.CharField(max_length=280)
    query = models.CharField(max_length=280)

    def __str__(self):
        return f"tweet: {self.id}"

    def insert(self, tweet: object, query: str) -> None:
        """Insert tweet and author if not already exist."""
        try:  # Check if tweet already exist
            tweet = Tweets.objects.get(id=tweet.id)
        except ObjectDoesNotExist:  # Insert tweet
            try:  # Check if author already exist
                author = TwitterUser.objects.get(id=tweet.author_id)
            except ObjectDoesNotExist:  # Insert author
                author = TwitterUser(id=tweet.author_id)
                author.save()
            tweet.data["author_id"] = author
            # FIND A WAY TO DEAL WITH referenced_tweets lenght > 1
            if tweet.data.get("referenced_tweets"):
                tweet.data["referenced_tweets_id"] = tweet.data[
                    "referenced_tweets"
                ][0]["id"]
                tweet.data["referenced_tweets_type"] = tweet.data[
                    "referenced_tweets"
                ][0]["type"]
                del tweet.data["referenced_tweets"]
            new_tweet = Tweets(**tweet.data)
            new_tweet.query = query
            new_tweet.save()

    def get_tweets_about(self, query: str) -> QuerySet:
        """Return tweets about query."""
        return Tweets.objects.filter(query=query)

    def get_conversations_about(self, query: str) -> dict:
        """
        Return conversations about query.

        conversations = {
            conversation_id: [tweet, ...],
            ...
        }
        """
        conversations = {}
        tweets = Tweets.objects.filter(
            query=query
        )  # .order_by("conversation_id")
        for tweet in tweets:
            if tweet.conversation_id not in conversations:

                conversations[tweet.conversation_id] = [
                    {
                        "id": tweet.id,
                        "author_id": str(tweet.author_id),
                        "text": tweet.text,
                        "lang": tweet.lang,
                        "created_at": str(tweet.created_at),
                        "public_metrics": tweet.public_metrics,
                        "referenced_tweets_id": tweet.referenced_tweets_id,
                        "referenced_tweets_type": tweet.referenced_tweets_type,
                        "conversation_id": tweet.conversation_id,
                        "in_reply_to_user_id": tweet.in_reply_to_user_id,
                        "source": tweet.source,
                    }
                ]
            else:
                conversations[tweet.conversation_id].append(
                    {
                        "id": tweet.id,
                        "author_id": str(tweet.author_id),
                        "text": tweet.text,
                        "lang": tweet.lang,
                        "created_at": str(tweet.created_at),
                        "public_metrics": tweet.public_metrics,
                        "referenced_tweets_id": tweet.referenced_tweets_id,
                        "referenced_tweets_type": tweet.referenced_tweets_type,
                        "conversation_id": tweet.conversation_id,
                        "in_reply_to_user_id": tweet.in_reply_to_user_id,
                        "source": tweet.source,
                    }
                )
        return conversations
