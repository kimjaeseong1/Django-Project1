# Generated by Django 4.0.3 on 2022-07-07 07:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0026_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 7, 50, 47, 499561, tzinfo=utc)),
        ),
    ]
