# Generated by Django 3.1.5 on 2021-02-09 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=145)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 55, 5, 303058, tzinfo=utc))),
                ('likes', models.IntegerField(default=0)),
                ('retweets', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
            ],
        ),
    ]
