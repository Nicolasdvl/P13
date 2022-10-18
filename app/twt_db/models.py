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

    def meta_query(self) -> dict:
        """
        Return metadata about query field for tag cloud.

        {
            query_name : n_query_in_db,
            ...
        }
        """
        query_tags = Tweets.objects.values_list("query", flat=True).distinct()
        return {
            tag: Tweets.objects.filter(query=tag).count() for tag in query_tags
        }

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

        dict formated for json.dumps().

        conversations = {
            conversation_id: {
                tweets: [
                    { ... },
                ],
                meta: { ... }
            },
            ...,
            meta: { ... }
        }
        """
        conversations = {}
        tweets = Tweets.objects.filter(query=query)
        list_conversations_id = tweets.values_list(
            "conversation_id", flat=True
        ).distinct()
        for tweet in tweets:
            if tweet.conversation_id not in conversations:
                ref_type = tweet.referenced_tweets_type  # for PEP8 E501
                conversations[tweet.conversation_id] = {
                    "tweets": [
                        {
                            "id": tweet.id,
                            "author_id": str(tweet.author_id),
                            "text": tweet.text,
                            "lang": tweet.lang,
                            "created_at": str(tweet.created_at),
                            "public_metrics": tweet.public_metrics,
                            "referenced_tweets_id": tweet.referenced_tweets_id,
                            "referenced_tweets_type": ref_type,
                            "conversation_id": tweet.conversation_id,
                            "in_reply_to_user_id": tweet.in_reply_to_user_id,
                            "source": tweet.source,
                        }
                    ],
                }
            else:
                conversations[tweet.conversation_id]["tweets"].append(
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
        conversations["meta"] = {
            "query": query,
            "count_tweets": tweets.count(),
            "count_conversations": len(conversations.keys()),
            "query_recurrence": tweets.filter(text__icontains=query).count(),
            "earliest_date": str(
                min(tweets.values_list("created_at", flat=True).distinct())
            ),
            "latest_date": str(
                max(tweets.values_list("created_at", flat=True).distinct())
            ),
        }
        for key in list_conversations_id:
            conversations[key]["meta"] = {
                "query_recurrence": tweets.filter(conversation_id=key)
                .filter(text__icontains=query)
                .count(),
                "earliest_date": str(
                    min(
                        tweets.filter(conversation_id=key)
                        .values_list("created_at", flat=True)
                        .distinct()
                    )
                ),
                "latest_date": str(
                    max(
                        tweets.filter(conversation_id=key)
                        .values_list("created_at", flat=True)
                        .distinct()
                    )
                ),
                "count_tweets": len(conversations[key]["tweets"]),
            }

        return conversations
