from django.test import TestCase
from tweepy import Tweet
from ..models import Tweets


class TestModels(TestCase):
    """Test Tweets and TwitterUser models from twt_db."""

    fixtures = ["test_tweets.json", "test_authors.json"]

    def setUp(self) -> None:
        """Setup for tests."""
        self.tweet_id = "123456789"
        self.tweet_data = {
            "author_id": "123",
            "id": self.tweet_id,
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
        self.tweet_from_tweepy = Tweet(self.tweet_data)

    def test_tweets_insert(self) -> None:
        """
        Test Tweets.insert().

        1/ A tweet saved should exist in database.
        """
        # Arrange
        tweets_model = Tweets()
        # Act
        tweets_model.insert(self.tweet_from_tweepy, "fake")
        # Assert
        Tweets.objects.get(id=self.tweet_id)

    def test_get_tweets_about(self) -> None:
        """
        Test Tweets.get_tweets_about().

        1/ According to fixtures, DB have 4 tweets with query "chat".
        """
        # Arrange
        tweets_model = Tweets()
        # Act
        tweets_about_cat = tweets_model.get_tweets_about("chat")
        # Assert
        self.assertEqual(len(tweets_about_cat), 4)

    def test_get_conversations_about(self) -> None:
        """
        Test Tweets.get_conversations_about().

        1/ dict meta should mention 2 conversations.
        2/ dict meta should mention 4 tweets.
        3/ dict conversation 1 should have 3 tweets.
        4/ dict conversation 2 should have 1 tweet.
        """
        # Arrange
        tweets_model = Tweets()
        conversation_id_1 = 31
        conversation_id_2 = 33
        # Act
        conversations_about_cat = tweets_model.get_conversations_about("chat")
        # Arrange
        self.assertEqual(
            conversations_about_cat["meta"]["count_conversations"], 2
        )
        self.assertEqual(conversations_about_cat["meta"]["count_tweets"], 4)
        self.assertEqual(
            len(conversations_about_cat[conversation_id_1]["tweets"]), 3
        )
        self.assertEqual(
            len(conversations_about_cat[conversation_id_2]["tweets"]), 1
        )
