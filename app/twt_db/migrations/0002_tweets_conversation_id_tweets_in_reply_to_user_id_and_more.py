# Generated by Django 4.1.1 on 2022-09-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twt_db", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweets",
            name="conversation_id",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="tweets",
            name="in_reply_to_user_id",
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="tweets",
            name="source",
            field=models.CharField(max_length=280, null=True),
        ),
    ]
