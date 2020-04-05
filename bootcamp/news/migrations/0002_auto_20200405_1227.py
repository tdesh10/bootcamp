# Generated by Django 3.0.3 on 2020-04-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='meta_description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta_url',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
