from django.db import models


class TwitterUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=280)

    def __str__(self):
        return f"author: {self.id}"


class Tweets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author_id = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    lang = models.CharField(max_length=2)
    created_at = models.DateTimeField()
    saved_at = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    public_metrics = models.CharField(max_length=500)
    referenced_tweets = models.CharField(max_length=500)

    def __str__(self):
        return f"tweet: {self.id}"
