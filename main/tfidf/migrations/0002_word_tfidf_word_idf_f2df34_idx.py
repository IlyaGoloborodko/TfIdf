# Generated by Django 4.2.11 on 2024-03-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfidf', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='word',
            index=models.Index(fields=['-idf'], name='tfidf_word_idf_f2df34_idx'),
        ),
    ]
