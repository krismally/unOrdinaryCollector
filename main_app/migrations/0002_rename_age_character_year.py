# Generated by Django 4.0.5 on 2022-07-10 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='age',
            new_name='year',
        ),
    ]
