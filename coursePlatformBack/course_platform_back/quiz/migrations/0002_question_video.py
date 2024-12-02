# Generated by Django 5.1.1 on 2024-10-12 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
        ("video", "0002_alter_video_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="video.video",
            ),
        ),
    ]
