# Generated by Django 3.2.9 on 2021-11-11 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20211111_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='exit',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='exit',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='history',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='logbook',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='logbook',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='unregisteredvehicle',
            name='ts_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='unregisteredvehicle',
            name='ts_updated',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
