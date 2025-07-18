# Generated by Django 5.0.6 on 2024-07-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translator", "0039_kagitranslator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kagitranslator",
            name="summarization_engine",
            field=models.CharField(
                default="cecil",
                help_text="Please check https://help.kagi.com/kagi/api/summarizer.html#summarization-engines",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="kagitranslator",
            name="summary_type",
            field=models.CharField(
                default="summary",
                help_text="Please check https://help.kagi.com/kagi/api/summarizer.html#summary-types",
                max_length=20,
            ),
        ),
    ]
