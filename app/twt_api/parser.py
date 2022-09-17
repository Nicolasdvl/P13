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
        self, query: str, max_result=10
    ) -> list | tweepy.TweepyException:
        """
        Return list of tweet object for a query.

        Tweet attr is defined in self.tweet_fields.
        Query is filter by lang:fr.
        """
        query += " lang:fr"
        try:
            response = self.client.search_recent_tweets(
                query, max_results=max_result, tweet_fields=self.tweet_fields
            )
            return response.data
        except tweepy.TweepyException as e:
            return e
