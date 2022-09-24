# Generated by Django 4.1.1 on 2022-09-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twt_db", "0003_tweets_query"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweets",
            name="referenced_tweets",
        ),
        migrations.AddField(
            model_name="tweets",
            name="referenced_tweets_id",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="tweets",
            name="referenced_tweets_type",
            field=models.CharField(max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name="tweets",
            name="conversation_id",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="tweets",
            name="in_reply_to_user_id",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="tweets",
            name="source",
            field=models.CharField(default="N/A", max_length=280),
            preserve_default=False,
        ),
    ]
