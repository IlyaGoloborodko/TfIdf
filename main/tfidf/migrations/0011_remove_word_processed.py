# Generated by Django 4.2.11 on 2024-03-31 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfidf', '0010_alter_worddocument_word_tf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='processed',
        ),
    ]