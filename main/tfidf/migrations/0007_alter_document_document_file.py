# Generated by Django 4.2.11 on 2024-03-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfidf', '0006_document_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.FileField(default=None, upload_to='documents/'),
        ),
    ]
