# Generated by Django 3.1.5 on 2021-02-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210209_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
