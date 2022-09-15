# Generated by Django 4.0.3 on 2022-07-07 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='club',
            name='pudate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='club',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]