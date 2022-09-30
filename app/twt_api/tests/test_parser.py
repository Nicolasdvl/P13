from unittest.mock import MagicMock
from django.test import TestCase
from ..parser import Parser


class ParserTestCase(TestCase):
    def setUp(self) -> None:
        self.parser = Parser()
        self.parser.get_fr_tweets_about = MagicMock(return_value="tweet")
        self.parser.get_conversation = MagicMock(return_value="conversation")

    def test_get_fr_tweets_about(self) -> None:
        # Arrange
        result = self.parser.get_fr_tweets_about("cat")
        # Assert
        self.assertEqual(result, "tweet")

    def test_get_conversation(self) -> None:
        # Arrange
        result = self.parser.get_conversation(123456789)
        # Assert
        self.assertEqual(result, "conversation")
