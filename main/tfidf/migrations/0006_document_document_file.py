# Generated by Django 4.2.11 on 2024-03-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfidf', '0005_remove_word_documents_document_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]