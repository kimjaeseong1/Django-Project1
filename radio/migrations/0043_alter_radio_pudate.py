# Generated by Django 4.0.3 on 2022-08-22 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0042_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 3, 46, 37, 217160, tzinfo=utc)),
        ),
    ]
