# Generated by Django 4.0.3 on 2022-03-16 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_merge_20220316_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
    ]
