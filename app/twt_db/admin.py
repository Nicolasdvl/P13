from django.contrib import admin
from .models import Tweets


class TweetsAdmin(admin.ModelAdmin):
    """Tweets visualisation for admin panel."""

    list_display = (
        "id",
        "author_id",
        "created_at",
        "conversation_id",
        "query",
    )
    list_display_links = ("id",)
    list_filter = ("conversation_id", "query")
    ordering = ("conversation_id",)

    def has_change_permission(self, request, object=None):
        """Disable edition for Tweets fields"""
        return False


admin.site.register(Tweets, TweetsAdmin)
