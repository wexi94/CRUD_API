# Generated by Django 3.2.5 on 2021-07-31 10:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apibasics', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 31, 10, 51, 31, 699622, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(default='Test@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='A', max_length=100),
            preserve_default=False,
        ),
    ]