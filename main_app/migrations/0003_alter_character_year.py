# Generated by Django 4.0.5 on 2022-07-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_age_character_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='year',
            field=models.FloatField(),
        ),
    ]
