# Generated by Django 3.0.5 on 2020-05-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0012_auto_20200505_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='sucess',
        ),
        migrations.AddField(
            model_name='mission',
            name='success_Goal',
            field=models.IntegerField(default=1),
        ),
    ]