import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


class Parser:
    """

    def __init__(self):
        self.url = "https://api.twitter.com/2/tweets/"
        self.header = {"key": "APIkey"}
        self.params = "params"

    def request_api(self, query: str = None) -> str:
        """ """
        if query:
            self.params["query"] = query
        try:
            response = requests.get(
                url=self.url, header=self.header, params=self.params
            )
        except requests.exceptions.RequestException as error:
            raise error
        return response.json()

     """

    def __init__(self) -> None:
        self.client = tweepy.Client(os.environ.get("TWITTER_BEARER"))
        self.tweet_fields = (
            "id, author_id, text, lang, created_at, public_metrics"
        )

    def get_tweets(
        self, query: str, max_result=10
    ) -> list | tweepy.TweepyException:
        """Return list of tweets object for a query"""
        try:
            response = self.client.search_recent_tweets(
                query, max_results=max_result, tweet_fields=self.tweet_fields
            )
            print("HERE", response.errors)
            return response.data
        except tweepy.TweepyException as e:
            return e
