# Generated by Django 4.0.3 on 2022-07-28 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_alter_diarys_soccer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaryimages',
            name='diary',
        ),
        migrations.AddField(
            model_name='diaryimages',
            name='diarys',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='soccer.diarys'),
        ),
    ]
