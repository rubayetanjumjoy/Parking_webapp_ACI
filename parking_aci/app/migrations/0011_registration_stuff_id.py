# Generated by Django 3.2.8 on 2021-10-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211010_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='stuff_id',
            field=models.TextField(default=''),
        ),
    ]
