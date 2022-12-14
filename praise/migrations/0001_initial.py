# Generated by Django 4.0.3 on 2022-06-21 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('제목', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='praise/%y/%m')),
                ('content', models.TextField()),
                ('작성자', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='작성자', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
