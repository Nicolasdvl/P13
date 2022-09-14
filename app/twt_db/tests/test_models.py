from django.test import TestCase
from tweepy import Tweet
from ..models import Tweets


class TestModels(TestCase):
    def setUp(self) -> None:
        self.tweet_from_tweepy = Tweet()
        self.tweet_from_tweepy.id = "123456789"
        self.tweet_from_tweepy.data = {
            "author_id": "123",
            "id": self.tweet_from_tweepy.id,
            "public_metrics": {
                "retweet_count": 28,
                "reply_count": 2,
                "like_count": 9,
                "quote_count": 0,
            },
            "text": "this is a fake tweet",
            "created_at": "2022-09-14T15:09:59.000Z",
            "lang": "fr",
        }

    def test_tweets_insert(self) -> None:
        """
        Test Tweets.insert().

        1/ A tweet saved should exist in database.
        """
        # Arrange
        tweets_model = Tweets()
        # Act
        tweets_model.insert(self.tweet_from_tweepy)
        # Assert
        tweets_model.objects.get(id=self.tweet_from_tweepy.id)
