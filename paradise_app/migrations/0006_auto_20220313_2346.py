# Generated by Django 3.2.7 on 2022-03-13 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paradise_app', '0005_auto_20220311_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 23, 46, 47, 105288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 23, 46, 47, 105288, tzinfo=utc)),
        ),
    ]
