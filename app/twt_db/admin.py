from django.contrib import admin
from .models import Tweets, TwitterUser

admin.site.register(Tweets)
admin.site.register(TwitterUser)
