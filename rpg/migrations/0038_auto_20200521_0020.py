# Generated by Django 3.0.6 on 2020-05-20 22:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0037_auto_20200521_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='mission_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 22, 20, 29, 938495, tzinfo=utc)),
        ),
    ]
