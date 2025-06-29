# Generated by Django 5.0.2 on 2024-02-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translator", "0016_alter_deeplwebtranslator_max_characters_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="translated_content",
            name="id",
        ),
        migrations.AlterField(
            model_name="translated_content",
            name="hash",
            field=models.BinaryField(
                max_length=8, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
