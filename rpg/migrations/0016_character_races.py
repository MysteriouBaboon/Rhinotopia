# Generated by Django 3.0.5 on 2020-05-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0015_auto_20200506_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='races',
            field=models.CharField(choices=[('EL', 'Elf'), ('OR', 'Ork')], default='EL', max_length=2),
        ),
    ]
