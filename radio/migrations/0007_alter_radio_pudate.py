# Generated by Django 4.0.3 on 2022-06-21 04:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0006_alter_radio_pudate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='pudate',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 4, 40, 5, 809541, tzinfo=utc)),
        ),
    ]