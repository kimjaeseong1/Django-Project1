# Generated by Django 4.0.3 on 2022-07-11 07:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0031_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 7, 40, 37, 76441, tzinfo=utc)),
        ),
    ]
