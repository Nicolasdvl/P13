from datetime import datetime
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


class Parser:
    """
    Parse data from Twitter API.

    Work with tweepy package. Parser.client.* to use tweepy method.
    """

    def __init__(self) -> None:
        """Initialize tweepy.Client."""
        self.client = tweepy.Client(os.environ.get("TWITTER_BEARER"))
        self.tweet_fields = (
            "id,author_id,text,lang,created_at,public_metrics,"
            "source,in_reply_to_user_id,conversation_id,referenced_tweets"
        )

    def get_fr_tweets_about(
        self, query: str, max_result: int = 10, start_time: datetime = None
    ) -> list:
        """
        Return list of tweet object for a query.

        Tweet attr is defined in self.tweet_fields.
        Query is filter by lang:fr.
        """
        query += " lang:fr"
        try:
            response = self.client.search_recent_tweets(
                query,
                max_results=max_result,
                tweet_fields=self.tweet_fields,
                start_time=start_time,
            )
            return response.data
        except tweepy.TweepyException as e:
            return e

    def get_conversation(
        self,
        conversation_id,
        max_result: int = 100,
        start_time: datetime = None,
    ) -> list:
        """
        Retrun a list of tweet object for a conversation.

        Tweet attr is defined in self.tweet_fields.
        """
        query = f"conversation_id:{conversation_id}"
        try:
            response = self.client.search_recent_tweets(
                query,
                max_results=max_result,
                tweet_fields=self.tweet_fields,
                start_time=start_time,
            )
            return response.data
        except tweepy.TweepyException as e:
            return e
