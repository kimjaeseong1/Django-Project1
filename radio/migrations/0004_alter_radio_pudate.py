# Generated by Django 4.0.3 on 2022-06-13 02:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 2, 12, 19, 190443, tzinfo=utc)),
        ),
    ]