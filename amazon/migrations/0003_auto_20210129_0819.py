# Generated by Django 3.1.4 on 2021-01-29 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0002_auto_20210128_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 8, 19, 36, 985628)),
        ),
    ]
