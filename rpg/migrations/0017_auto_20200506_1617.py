# Generated by Django 3.0.5 on 2020-05-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0016_character_races'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='races',
            field=models.CharField(choices=[('EL', 'Elf'), ('OR', 'Ork'), ('HU', 'Human')], default='EL', max_length=2),
        ),
    ]
