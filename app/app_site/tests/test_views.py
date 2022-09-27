from django.test import Client, TestCase


class TestAppViews(TestCase):
    """Test views for app_site."""

    fixtures = ["test_tweets.json", "test_authors.json"]

    def setUp(self):
        """Initiate django client test."""
        self.client = Client()

    def test_get_index(self):
        """
        Test index view with GET request.

        1/ GET status should be 200.
        2/ GET context should have cloud_json.
        """
        # Arrange
        assert_context = '{"chat": 4, "chien": 1}'
        # Act
        response = self.client.get("/")
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cloud_json"], assert_context)

    def test_post_index(self):
        """
        Test index view with POST request.

        1/ POST query existing in db should return status 200.
        2/ POST query existing in db should return context with
        conversations_json.
        """
        # Arrange
        data_in_db = {"q": "chat"}
        # Act
        response = self.client.post("/", data=data_in_db)
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["conversations_json"])
