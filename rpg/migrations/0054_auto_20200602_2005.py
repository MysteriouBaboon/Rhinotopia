# Generated by Django 3.0.6 on 2020-06-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0053_auto_20200602_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(default='Unspecified', max_length=20),
        ),
    ]
