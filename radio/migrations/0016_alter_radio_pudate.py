# Generated by Django 4.0.3 on 2022-06-23 06:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0015_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 6, 48, 13, 833128, tzinfo=utc)),
        ),
    ]
