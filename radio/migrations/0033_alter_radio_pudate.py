# Generated by Django 4.0.3 on 2022-07-18 05:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0032_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 18, 5, 31, 47, 738030, tzinfo=utc)),
        ),
    ]
