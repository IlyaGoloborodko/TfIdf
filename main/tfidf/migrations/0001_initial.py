# Generated by Django 4.2.11 on 2024-03-27 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('total_occurences', models.IntegerField(default=0)),
                ('idf', models.FloatField(default=0.0)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-idf'],
            },
        ),
        migrations.CreateModel(
            name='Word_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_tf', models.IntegerField(default=0)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tfidf.document')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tfidf.word')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='documents',
            field=models.ManyToManyField(through='tfidf.Word_Document', to='tfidf.document'),
        ),
    ]
