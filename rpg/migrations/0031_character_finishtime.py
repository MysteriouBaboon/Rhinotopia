# Generated by Django 3.0.6 on 2020-05-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0030_mission_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='finishtime',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]