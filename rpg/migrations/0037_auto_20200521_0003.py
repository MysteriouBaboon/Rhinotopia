# Generated by Django 3.0.6 on 2020-05-20 22:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0036_auto_20200520_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='finishTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 22, 3, 42, 720358, tzinfo=utc)),
        ),
    ]
