# Generated by Django 4.1 on 2022-08-18 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publisedDate',
            field=models.DateField(default=datetime.datetime(2022, 8, 18, 0, 25, 5, 79484), verbose_name='Published At'),
        ),
    ]
