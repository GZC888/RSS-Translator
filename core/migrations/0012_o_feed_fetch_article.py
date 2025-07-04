# Generated by Django 5.0.4 on 2024-04-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_o_feed_quality"),
    ]

    operations = [
        migrations.AddField(
            model_name="o_feed",
            name="fetch_article",
            field=models.BooleanField(
                default=False,
                help_text="Fetch original article from the website.",
                verbose_name="Fetch Original Article",
            ),
        ),
    ]
