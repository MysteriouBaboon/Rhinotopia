# Generated by Django 3.0.6 on 2020-06-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0052_auto_20200526_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='specie',
            new_name='species',
        ),
        migrations.AlterField(
            model_name='character',
            name='available_point',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='hp',
            field=models.IntegerField(default=3),
        ),
    ]