# Generated by Django 4.0.3 on 2022-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_profile_expense_current_profile_expense_last_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.BigIntegerField(null=True),
        ),
    ]