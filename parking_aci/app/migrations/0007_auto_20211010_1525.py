# Generated by Django 3.2.8 on 2021-10-10 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_logbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logbook',
            name='entry_time',
        ),
        migrations.RemoveField(
            model_name='logbook',
            name='exit_time',
        ),
        migrations.AddField(
            model_name='logbook',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='logbook',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
