# Generated by Django 4.0.2 on 2022-03-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_remove_profile_id_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hall_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='room_no',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_prof',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
