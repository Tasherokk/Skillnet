# Generated by Django 5.1.2 on 2024-11-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatgpt_agent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversationhistory",
            name="thread_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
