# Generated by Django 4.2.11 on 2024-03-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfidf', '0008_remove_word_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
