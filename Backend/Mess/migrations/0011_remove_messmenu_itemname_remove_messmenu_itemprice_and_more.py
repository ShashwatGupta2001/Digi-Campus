# Generated by Django 4.0.3 on 2022-03-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0010_messorder_ordereddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messmenu',
            name='itemName',
        ),
        migrations.RemoveField(
            model_name='messmenu',
            name='itemPrice',
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_1',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_2',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_3',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_4',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_5',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='extras_6',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='messmenu',
            name='price_6',
            field=models.IntegerField(null=True),
        ),
    ]
