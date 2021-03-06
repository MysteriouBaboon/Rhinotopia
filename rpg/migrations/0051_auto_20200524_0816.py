# Generated by Django 3.0.6 on 2020-05-24 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0050_auto_20200523_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='regenDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 16, 44, 511079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='character',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 16, 44, 511079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='character',
            name='respawnDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 16, 44, 511079, tzinfo=utc)),
        ),
    ]
