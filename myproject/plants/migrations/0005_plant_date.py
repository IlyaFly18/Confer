# Generated by Django 3.1 on 2020-11-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20201104_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
