# Generated by Django 3.1.5 on 2021-02-09 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 16, 55, 9, 42249, tzinfo=utc)),
        ),
    ]
